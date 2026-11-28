import pandas as pd
import sqlite3
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the validated dataset
input_file = project_folder / "data" / "cleaned" / "dataset_enriched.csv"
df = pd.read_csv(input_file)

# Create the SQLite database
database_file = project_folder / "customer_database.db"
connection = sqlite3.connect(database_file)

# Load data into a database table
df.to_sql("customers", connection, if_exists="replace", index=False)

# Check the number of records loaded
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM customers")
total_records = cursor.fetchone()[0]

connection.close()

print("Data loading complete!")
print("Records loaded:", total_records)
print("Database saved to:", database_file)