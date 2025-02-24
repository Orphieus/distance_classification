import os
from pathlib import Path
from nbformat import read

# File to check
notebook_file = "Lab5.ipynb"  # Replace with your notebook's filename

# Verify the notebook exists
if not os.path.exists(notebook_file):
    print(f"Notebook file '{notebook_file}' not found.")
    exit(1)

# Parse the notebook
with open(notebook_file, 'r', encoding='utf-8') as f:
    nb = read(f, as_version=4)

# Find all file references
errors = []
for cell in nb.cells:
    if cell.cell_type == "code":
        for line in cell.source.splitlines():
            if "open(" in line or "imread(" in line:
                # Extract potential file paths
                potential_file = line.split("(")[1].split(")")[0].strip("'\"")
                if not os.path.exists(potential_file):
                    errors.append(f"Missing file: {potential_file}")

# Report results
if errors:
    print("Some files are missing:")
    for error in errors:
        print(f" - {error}")
    exit(1)
else:
    print("All files and images load successfully.")
