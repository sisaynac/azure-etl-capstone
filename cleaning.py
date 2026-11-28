import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the stored dataset
input_file = project_folder / "data" / "cleaned" / "dataset_storage.csv"
df = pd.read_csv(input_file)

# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Remove extra spaces from text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# Save cleaned dataset
output_file = project_folder / "data" / "cleaned" / "dataset_cleaned.csv"
df.to_csv(output_file, index=False)

print("\nData cleaning complete!")
print("Rows after cleaning:", len(df))
print("Saved to:", output_file)