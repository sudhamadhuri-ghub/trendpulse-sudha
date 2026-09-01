import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

# Load data/trends_analysed.csv into a DataFrame
df_analysed = pd.read_csv('data/trends_analysed.csv')
print(f"Loaded {len(df_analysed)} stories from data/trends_analysed.csv")

# Create a folder called outputs/ if it doesn't exist
Path("outputs/").mkdir(parents=True, exist_ok=True)
print("Created 'outputs/' directory if it didn't exist.")

#Chart 1: Top 10 Stories by Score

# Sort by score and get the top 10 stories
top_10_stories = df_analysed.nlargest(10, 'score')

# Shorten titles longer than 50 characters
top_10_stories['short_title'] = top_10_stories['title'].apply(lambda x: x[:50] + '...' if len(x) > 50 else x)

plt.figure(figsize=(12, 8))
sns.barplot(x='score', y='short_title', data=top_10_stories, palette='viridis')
plt.title('Top 10 Stories by Score')
plt.xlabel('Score')
plt.ylabel('Story Title')
plt.tight_layout()
plt.savefig('outputs/chart1_top_stories.png')
plt.show()

#Chart 2: Stories per Category

# Count stories per category
category_counts = df_analysed['category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

plt.figure(figsize=(12, 7))
sns.barplot(x='Category', y='Count', data=category_counts, palette='tab10')
plt.title('Number of Stories per Category')
plt.xlabel('Category')
plt.ylabel('Number of Stories')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('outputs/chart2_categories.png')
plt.show()

#Chart 3: Score vs Comments

plt.figure(figsize=(10, 8))
sns.scatterplot(x='score', y='num_comments', hue='is_popular', data=df_analysed, palette='coolwarm', s=100, alpha=0.7)
plt.title('Story Score vs. Number of Comments (Popularity)')
plt.xlabel('Score')
plt.ylabel('Number of Comments')
plt.legend(title='Is Popular')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('outputs/chart3_scatter.png')
plt.show()

#Dashboard

fig, axes = plt.subplots(1, 3, figsize=(25, 8))
fig.suptitle('TrendPulse Dashboard', fontsize=20, y=1.02)

# Chart 1: Top 10 Stories by Score
sns.barplot(x='score', y='short_title', hue='short_title', data=top_10_stories, palette='viridis', legend=False, ax=axes[0])
axes[0].set_title('Top 10 Stories by Score')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Story Title')

# Chart 2: Stories per Category
sns.barplot(x='Category', y='Count', hue='Category', data=category_counts, palette='tab10', legend=False, ax=axes[1])
axes[1].set_title('Number of Stories per Category')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Number of Stories')
axes[1].tick_params(axis='x', rotation=45)

# Chart 3: Score vs Comments
sns.scatterplot(x='score', y='num_comments', hue='is_popular', data=df_analysed, palette='coolwarm', s=100, alpha=0.7, ax=axes[2])
axes[2].set_title('Story Score vs. Number of Comments (Popularity)')
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Number of Comments')
axes[2].legend(title='Is Popular')
axes[2].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
fig.subplots_adjust(top=0.9)
plt.savefig('outputs/dashboard.png')
plt.show()
