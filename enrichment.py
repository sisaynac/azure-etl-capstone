import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the cleaned dataset
input_file = project_folder / "data" / "cleaned" / "dataset_cleaned.csv"
df = pd.read_csv(input_file)

# Create a purchase category
df["PurchaseCategory"] = pd.cut(
    df["PurchaseAmount"],
    bins=[-float("inf"), 100, 500, float("inf")],
    labels=["Low", "Medium", "High"],
    right=False
)

# Save the enriched dataset
output_file = project_folder / "data" / "cleaned" / "dataset_enriched.csv"
df.to_csv(output_file, index=False)

print("Data enrichment complete!")
print("Total rows:", len(df))
print("\nPurchase categories:")
print(df["PurchaseCategory"].value_counts())
print("Saved to:", output_file)