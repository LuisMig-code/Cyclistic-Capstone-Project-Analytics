import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("shane3martin/cyclist-capstone-project")

print("Path to dataset files:", path)

# set de end path file
end_path = "data/raw"
os.makedirs(end_path, exist_ok=True)

# Copy the files
for file in os.listdir(path):
    shutil.copy2(
        os.path.join(path, file), 
        os.path.join(end_path, file)
    )
    
print(f"files copied to: {end_path}")