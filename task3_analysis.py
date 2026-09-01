import pandas as pd
import numpy as np

# Load data/trends_clean.csv into a Pandas DataFrame
df_analysed = pd.read_csv('data/trends_clean.csv')
print(f"Loaded {len(df_analysed)} stories from data/trends_clean.csv")

# Print the first 5 rows
print("\nFirst 5 rows of the DataFrame:")
display(df_analysed.head())

# Print the shape of the DataFrame (rows and columns)
print("\nShape of the DataFrame (rows, columns):")
print(df_analysed.shape)

# Print the average score and average num_comments across all stories
avg_score = df_analysed['score'].mean()
avg_comments = df_analysed['num_comments'].mean()
print(f"\nAverage Score: {avg_score:.2f}")
print(f"Average Number of Comments: {avg_comments:.2f}")

# Basic Analysis with NumPy
print("\n--- Basic Analysis with NumPy ---")
# Mean, median, and standard deviation of score
mean_score = np.mean(df_analysed['score'])
median_score = np.median(df_analysed['score'])
std_dev_score = np.std(df_analysed['score'])
print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
print(f"Standard Deviation of Score: {std_dev_score:.2f}")

# Highest and lowest score
highest_score = np.max(df_analysed['score'])
lowest_score = np.min(df_analysed['score'])
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

# Which category has the most stories?
most_common_category = df_analysed['category'].mode()[0]
print(f"Category with the most stories: {most_common_category}")

# Which story has the most comments? Print its title and comment count.
most_comments_story = df_analysed.loc[df_analysed['num_comments'].idxmax()]
print(f"Story with the most comments: '{most_comments_story['title']}' (Comments: {most_comments_story['num_comments']})")

# Add New Columns
print("\n--- Adding New Columns ---")
# engagement: num_comments / (score + 1)
df_analysed['engagement'] = df_analysed['num_comments'] / (df_analysed['score'] + 1)

# is_popular: True if score > average score, else False
df_analysed['is_popular'] = df_analysed['score'] > avg_score

print("DataFrame with new 'engagement' and 'is_popular' columns (first 5 rows):")
display(df_analysed.head())

# Save the Result
print("\n--- Saving the Result ---")
cleaned_analysed_filename = 'data/trends_analysed.csv'
df_analysed.to_csv(cleaned_analysed_filename, index=False)
print(f"Saved {len(df_analysed)} rows to {cleaned_analysed_filename}")
