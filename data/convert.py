import pandas as pd

# Load CSV
df = pd.read_csv("netflix_titles.csv")

# Convert to JSON
df.to_json(
    "netflix_titles.json",
    orient="records",
    indent=4
)

print("CSV converted to JSON successfully!")