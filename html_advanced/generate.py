#!/usr/bin/python3
import shutil
from pathlib import Path

# Find the highest existing index number
files = list(Path(".").glob("*-index.html"))

if not files:
    # First run: create the original HTML file
    number = 0

    content = """<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
"""

    Path("0-index.html").write_text(content)
    print("Created 0-index.html")

else:
    # Find the latest numbered file
    numbers = [
        int(f.name.split("-")[0])
        for f in files
        if f.name.split("-")[0].isdigit()
    ]

    latest = max(numbers)
    next_number = latest + 1

    source = Path(f"{latest}-index.html")
    destination = Path(f"{next_number}-index.html")

    # Copy the latest file into the next one
    shutil.copy2(source, destination)

    print(f"Copied {source} to {destination}")
