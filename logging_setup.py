import logging
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Create the logs folder if needed
logs_folder = project_folder / "logs"
logs_folder.mkdir(parents=True, exist_ok=True)

# Set the log file
log_file = logs_folder / "pipeline.log"

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# Record pipeline activity
logging.info("Data pipeline started.")
logging.info("Data cleaning completed.")
logging.info("Data enrichment completed.")
logging.info("Data validation completed.")
logging.info("Database loading completed.")
logging.info("Data pipeline completed successfully.")

print("Monitoring and logging setup complete!")
print("Log file saved to:", log_file)