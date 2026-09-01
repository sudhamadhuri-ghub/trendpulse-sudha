import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Convert top_25_categories to a DataFrame for easier plotting
category_df = pd.DataFrame(top_25_categories, columns=['Category', 'Count'])

plt.figure(figsize=(12, 7))
sns.barplot(x='Category', y='Count', data=category_df, palette='viridis')
plt.title('Distribution of Collected Stories by Category (Top 25)', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Number of Stories', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()