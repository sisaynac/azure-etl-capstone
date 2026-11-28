import subprocess
import sys
import logging
from pathlib import Path

# Find project folder
project_folder = Path(__file__).resolve().parent.parent
scripts_folder = project_folder / "scripts"

# Create logs folder
logs_folder = project_folder / "logs"
logs_folder.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=logs_folder / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# Scripts to run in order
scripts = [
    "cleaning.py",
    "enrichment.py",
    "validation.py",
    "loading.py"
]

logging.info("Pipeline started.")

try:
    for script in scripts:
        logging.info("Running %s", script)

        result = subprocess.run(
            [sys.executable, str(scripts_folder / script)],
            cwd=project_folder,
            check=True
        )

        logging.info("%s completed successfully.", script)

    logging.info("Pipeline completed successfully!")
    print("PIPELINE COMPLETED SUCCESSFULLY!")

except subprocess.CalledProcessError as error:
    logging.error("Pipeline failed: %s", error)
    print("PIPELINE FAILED! Check logs for details.")
    sys.exit(1)