import pandas as pd

current_date = datetime.now().strftime("%Y%m%d")
output_filename = f"data/trends_{current_date}.json"  # file name in data/trends_YYYYMMDD.json format

# Load the JSON file into a Pandas DataFrame
df_stories = pd.read_json(output_filename)

# 1. Remove duplicate rows based on 'post_id'
df_stories.drop_duplicates(subset=['post_id'], inplace=True)
print(f"After removing duplicates: {len(df_stories)}")

# 2. Drop rows where 'post_id', 'title', or 'score' is missing
df_stories.dropna(subset=['post_id', 'title', 'score'], inplace=True)
print(f"After removing nulls: {len(df_stories)}")

# 3. Convert 'score' and 'num_comments' to integers
df_stories['score'] = df_stories['score'].astype(int)
df_stories['num_comments'] = df_stories['num_comments'].astype(int)

# 4. Remove stories where 'score' is less than 5
df_stories = df_stories[df_stories['score'] >= 5]
print(f"After removing low scores: {len(df_stories)}")

# 5. Strip extra spaces from the 'title' column
df_stories['title'] = df_stories['title'].str.strip()


# Save the cleaned DataFrame to data/trends_clean.csv
cleaned_output_filename = 'data/trends_clean.csv'
df_stories.to_csv(cleaned_output_filename, index=False)

# Print a confirmation message with the number of rows saved
print(f"Saved {len(df_stories)} rows to {cleaned_output_filename}")

# Print a quick summary: how many stories per category
print("\nStories per category:")
print(df_stories['category'].value_counts().sort_index())
