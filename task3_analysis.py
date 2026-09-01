

# Create data directory if it doesn't exist
Path("data/").mkdir(parents=True, exist_ok=True)

# Define filename with current date
current_date = datetime.now().strftime("%Y%m%d")
output_filename = f"data/trends_{current_date}.json"  # file name in data/trends_YYYYMMDD.json format

# Save stories to JSON file
with open(output_filename, 'w') as f:
    json.dump(stories, f, indent=4)

print(f"Collected {len(stories)} stories. Saved to {output_filename}")    