# Cyclistic Capstone Project - Analytics

A comprehensive data analytics project for the Cyclistic bike-sharing case study, featuring automated data pipelines, exploratory data analysis, interactive dashboards, and business insights.

## 📋 Overview

This project analyzes Cyclistic's bike-sharing data to understand user behavior patterns and provide actionable insights for business growth. The analysis focuses on comparing casual riders vs. annual members to develop targeted marketing strategies.

## 🎯 Project Goals

- Analyze bike usage patterns between casual riders and annual members
- Identify key differences in riding behavior, duration, and station preferences
- Create interactive visualizations and dashboards for stakeholder presentations
- Develop automated data processing pipelines for reproducible analysis

## 🏗️ Project Structure

```
cyclistic-capstone-project/
├── data/
│   ├── raw/                    # Original datasets from Kaggle
│   └── processed/              # Cleaned and transformed data
├── notebooks/                  # Jupyter notebooks for analysis
│   ├── 01_data_preparation_temp.ipynb
│   ├── 02_data_quality_outliers_temp.ipynb
│   ├── 03_exploratory_analysis_temp.ipynb
│   ├── 04_data_validation_summary.ipynb
│   └── 05_powerbi_checks_temp.ipynb
├── pipelines/
│   ├── python/                 # Python data processing scripts
│   │   ├── colect_data.py
│   │   └── transform_data.py
│   └── n8n/                    # N8N workflow automation
├── reports/
│   ├── figures/                # Generated charts and plots
│   ├── mapa_interativo_end.html    # Interactive end station map
│   └── mapa_interativo_start.html  # Interactive start station map
├── dashboards/
│   ├── assets/                 # Dashboard assets
│   ├── powerbi/                # Power BI files
│   └── docs/                   # Dashboard documentation
├── src/                        # Source code modules
│   ├── ingestions/             # Data ingestion utilities
│   ├── metrics/                # Business metrics calculations
│   ├── transformation/         # Data transformation functions
│   ├── utils/                  # Utility functions
│   ├── validation/             # Data validation checks
│   └── visualization/          # Visualization helpers
├── sql/                        # SQL queries and scripts
├── tests/                      # Unit tests
├── pyproject.toml             # Project configuration
├── requirements.txt           # Python dependencies
└── README.md
```

## 🚀 Features

### Data Processing Pipeline
- **Automated Data Collection**: Downloads datasets from Kaggle using kagglehub
- **Data Cleaning**: Handles missing values, outliers, and data quality issues
- **Feature Engineering**: Creates derived metrics like ride duration, distance, and time features
- **Data Validation**: Comprehensive checks for data integrity

### Exploratory Data Analysis
- **Statistical Analysis**: Comprehensive descriptive statistics
- **User Behavior Analysis**: Compares casual vs. member riding patterns
- **Geospatial Analysis**: Interactive maps showing station usage patterns
- **Temporal Analysis**: Hourly, daily, and seasonal usage trends

### Interactive Dashboards
- **Power BI Dashboards**: Business intelligence visualizations
- **Interactive Maps**: HTML-based maps for start/end station analysis
- **Custom Visualizations**: Matplotlib, Seaborn, and Plotly charts

## 🛠️ Technology Stack

- **Python 3.10+**
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly, PyDeck
- **Web Scraping**: BeautifulSoup4, Requests, HTTPX
- **Jupyter Ecosystem**: JupyterLab, Notebook, Voila
- **Development Tools**: Black, Ruff, Pytest
- **Automation**: N8N workflows

## 📊 Data Sources

- **Primary Dataset**: Cyclistic trip data (August 2020)
- **Source**: Kaggle dataset by shane3martin
- **Original Features**: ride_id, rideable_type, timestamps, station info, coordinates, user type

## 🔄 Data Pipeline

1. **Data Collection**: Automated download from Kaggle
2. **Data Preparation**: Initial cleaning and null value handling
3. **Quality Checks**: Outlier detection and removal
4. **Feature Engineering**: Distance calculations, time features
5. **Exploratory Analysis**: Statistical analysis and visualizations
6. **Validation**: Final data quality checks
7. **Reporting**: Generate dashboards and interactive maps

## 📈 Key Findings

- **Data Loss**: ~13% of original data removed due to quality issues and outliers
- **New Features**: Added ride duration, distance, and temporal features
- **User Insights**: Distinct patterns between casual and member users
- **Geospatial Patterns**: Popular stations and routes identified

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Kaggle account (for data download)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cyclistic-capstone-project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   # For development dependencies
   pip install -e ".[dev]"
   ```

### Data Setup

1. **Download data**
   ```bash
   python pipelines/python/colect_data.py
   ```

2. **Run data processing pipeline**
   ```bash
   python pipelines/python/transform_data.py
   ```

### Running Analysis

1. **Launch Jupyter Lab**
   ```bash
   jupyter lab
   ```

2. **Execute notebooks in order**
   - `01_data_preparation_temp.ipynb`
   - `02_data_quality_outliers_temp.ipynb`
   - `03_exploratory_analysis_temp.ipynb`
   - `04_data_validation_summary.ipynb`

## 📊 Viewing Results

- **Interactive Maps**: Open `reports/mapa_interativo_start.html` and `reports/mapa_interativo_end.html`
- **Power BI Dashboard**: Open files in `dashboards/powerbi/`
- **Generated Figures**: View charts in `reports/figures/`

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

## 📝 Development

### Code Quality
- **Linting**: `ruff check .`
- **Formatting**: `black .`
- **Type Checking**: Configure your IDE for Python type hints

### Adding New Features
1. Create feature branch
2. Add code in appropriate `src/` module
3. Add tests in `tests/`
4. Update documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 👤 Author

**Luis Miguel**

## 🙏 Acknowledgments

- Cyclistic (Divvy) for providing the dataset
- Kaggle community for data hosting
- Open source Python data science ecosystem

## 📞 Contact

For questions or feedback about this project, please open an issue on GitHub.
