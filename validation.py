import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the enriched dataset
input_file = project_folder / "data" / "cleaned" / "dataset_enriched.csv"
df = pd.read_csv(input_file)

print("DATA VALIDATION REPORT")
print("----------------------")

# Check total records
print("Total records:", len(df))

# Check required columns
required_columns = [
    "CustomerID", "Name", "Age",
    "PurchaseAmount", "Country", "Date",
    "PurchaseCategory"
]

missing_columns = [col for col in required_columns if col not in df.columns]

print("Missing columns:", missing_columns)

# Check missing values
print("Missing values:", df.isnull().sum().sum())

# Check duplicate records
print("Duplicate records:", df.duplicated().sum())

# Check invalid purchase amounts
print("Negative purchase amounts:", (df["PurchaseAmount"] < 0).sum())

# Check purchase categories
print("\nPurchase category counts:")
print(df["PurchaseCategory"].value_counts())

print("\nData validation complete!")