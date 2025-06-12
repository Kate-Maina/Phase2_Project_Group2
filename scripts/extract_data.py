import os
import zipfile
import shutil
from pathlib import Path

# Folders containing your zip files
ZIPPED_DIRS = [Path("ZippedData_part1"), Path("ZippedData_part2")]
DATA_DIR = Path("Data")

# Skip extraction if the Data/ folder already exists
if DATA_DIR.exists():
    print("Data folder already exists. Skipping extraction.")
    exit(0)

# Create the Data/ folder
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Loop through each folder and extract zip files
for ZIPPED_DIR in ZIPPED_DIRS:
    for zip_path in ZIPPED_DIR.glob("*.zip"):
        print(f"Processing {zip_path.name} from {ZIPPED_DIR.name}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            temp_extract_path = ZIPPED_DIR / "temp_extracted"
            zip_ref.extractall(temp_extract_path)

            for root, _, files in os.walk(temp_extract_path):
                for file in files:
                    # Only copy valid data file types
                    if file.endswith((".csv", ".json", ".xlsx", ".xls", ".sqlite", ".db", ".txt")):
                        src = Path(root) / file
                        dest = DATA_DIR / file

                        if dest.exists():
                            print(f"{file} already exists. Skipping.")
                        else:
                            shutil.copy2(src, dest)
                            print(f"Extracted: {file}")

            shutil.rmtree(temp_extract_path)

print("All valid data files extracted into the Data/ folder.")
