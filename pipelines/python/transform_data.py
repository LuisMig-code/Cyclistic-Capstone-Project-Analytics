import pandas as pd
import numpy as np
import logging
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

print(BASE_DIR)

# Configuração de log para acompanhamento da automação
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calcular_haversine(lat1, lon1, lat2, lon2):
    """
    Calcula a distância Haversine vetorizada entre dois pontos na Terra.
    """
    R = 6371.0 # Raio da Terra em km
    
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    return R * c

def extract_data(file_path):
    """Lê os dados brutos."""
    logging.info(f"Lendo dados do arquivo: {file_path}")
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Aplica as regras de limpeza primárias: remoção de nulos, 
    remoção de duplicadas e correção de datas invertidas.
    """
    logging.info(f"Linhas iniciais: {len(df)}")
    
    # 1. Remoção de Nulos (Conforme insight de que a recuperação de coordenadas não compensava)
    df = df.dropna().copy()
    logging.info(f"Linhas após dropna: {len(df)}")
    
    # 2. Remover Duplicadas
    df = df.drop_duplicates(subset="ride_id")
    
    # 3. Conversão de tipos de data
    df['started_at'] = pd.to_datetime(df['started_at'], format='%Y-%m-%d %H:%M:%S')
    df['ended_at'] = pd.to_datetime(df['ended_at'], format='%Y-%m-%d %H:%M:%S')
    
    # 4. Remover inconsistências de tempo (started_at > ended_at)
    df = df[df['started_at'] <= df['ended_at']]
    logging.info(f"Linhas após limpeza de datas e duplicadas: {len(df)}")
    
    return df

def engineer_features(df):
    """Cria as novas colunas de negócio e tempo."""
    logging.info("Criando novas features...")
    
    # Tipo de trajeto
    df['round_trip'] = np.where(
        df['start_station_name'] == df['end_station_name'], 
        'same_place', 
        'different_place'
    )
    
    # Features de Duração
    df['ride_duration'] = df['ended_at'] - df['started_at']
    df['ride_duration_minutes'] = df['ride_duration'].dt.total_seconds() / 60
    
    # Features de Tempo
    df['week_day'] = df['started_at'].dt.day_name()
    df['is_weekend'] = df['started_at'].dt.dayofweek >= 5
    df['hour_start'] = df['started_at'].dt.hour
    df['hour_end'] = df['ended_at'].dt.hour
    
    # Features de Distância
    df['distance_km'] = calcular_haversine(
        df['start_lat'], df['start_lng'], 
        df['end_lat'], df['end_lng']
    )
    df['distance_m'] = df['distance_km'] * 1000
    
    return df

def remove_outliers_iqr(df):
    """
    Remove outliers de duração e distância separadamente para 
    viagens de ida e volta ('same_place') e ponto a ponto ('different_place').
    """
    logging.info("Calculando e removendo outliers (Método IQR)...")
    df['is_outlier'] = False
    
    trip_types = ['different_place', 'same_place']
    cols_to_check = ['ride_duration_minutes', 'distance_km']
    
    total_outliers = 0
    
    for trip_type in trip_types:
        for col in cols_to_check:
            mask = df['round_trip'] == trip_type
            subset = df[mask][col]
            
            Q1 = subset.quantile(0.25)
            Q3 = subset.quantile(0.75)
            IQR = Q3 - Q1
            
            limite_superior = Q3 + 1.5 * IQR
            limite_inferior = Q1 - 1.5 * IQR
            
            outliers_mask = mask & ((df[col] > limite_superior) | (df[col] < limite_inferior))
            df['is_outlier'] = df['is_outlier'] | outliers_mask
            
            qtd = outliers_mask.sum()
            total_outliers += qtd
            logging.info(f"[{trip_type}] {col}: {qtd} outliers detectados.")
            
    # Filtra e remove a coluna de apoio
    df_clean = df[~df['is_outlier']].drop(columns=['is_outlier']).copy()
    logging.info(f"Total de outliers removidos: {total_outliers}. Linhas finais: {len(df_clean)}")
    
    return df_clean

def run_etl(input_path, output_path):
    """Orquestra o pipeline ETL."""
    logging.info("=== INICIANDO PIPELINE ETL ===")
    
    # Extract
    df_raw = extract_data(input_path)
    
    # Transform
    df_cleaned = clean_data(df_raw)
    df_features = engineer_features(df_cleaned)
    df_final = remove_outliers_iqr(df_features)
    
    # Load
    logging.info(f"Exportando dados processados para: {output_path}")
    df_final.to_csv(output_path, index=False)
    
    logging.info("=== PIPELINE ETL CONCLUÍDO COM SUCESSO ===")

if __name__ == "__main__":
    # Definição dos caminhos dos arquivos
    INPUT_FILE = os.path.join(BASE_DIR, "data", "raw", "202008-divvy-tripdata.csv")
    OUTPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "dataset_final_limpo.csv")
    
    # Execução
    run_etl(INPUT_FILE, OUTPUT_FILE)