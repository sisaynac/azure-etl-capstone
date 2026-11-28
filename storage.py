import pandas as pd
from pathlib import Path

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the raw dataset
raw_file = project_folder / "data" / "raw" / "dataset.csv"

# Create the cleaned folder
cleaned_folder = project_folder / "data" / "cleaned"
cleaned_folder.mkdir(parents=True, exist_ok=True)

# Read the dataset
df = pd.read_csv(raw_file)

# Save a copy in the cleaned folder
output_file = cleaned_folder / "dataset_storage.csv"
df.to_csv(output_file, index=False)

print("Data storage complete!")
print("Rows:", len(df))
print("Saved to:", output_file)