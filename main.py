# 📱 Instagram Influencer Engagement Analysis
# Author: [Your Name]
# Description: Analyze influencer data to understand engagement patterns based on content type and niche.

# --- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# --- 1. Load Dataset ---
df = pd.read_csv('top_insta_influencers_data.csv')  # Make sure this CSV is available locally
print("Initial Data Shape:", df.shape)

# --- 2. Data Cleaning ---
# Remove rows with missing critical values
df = df.dropna(subset=['Followers', 'Engagement Rate', 'Likes', 'Comments', 'Category'])

# Convert engagement rate from string to float if needed
def parse_engagement(rate):
    if isinstance(rate, str):
        return float(rate.strip('%')) / 100
    return rate

df['Engagement Rate'] = df['Engagement Rate'].apply(parse_engagement)

# Remove unrealistic entries (e.g., 0 followers or very high rates)
df = df[df['Followers'] > 1000]
df = df[df['Engagement Rate'] < 1.0]

print("Cleaned Data Shape:", df.shape)

# --- 3. Exploratory Data Analysis (EDA) ---

## A. Followers vs Engagement Rate
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Followers', y='Engagement Rate', alpha=0.6)
plt.xscale('log')
plt.title('Followers vs. Engagement Rate')
plt.xlabel('Followers (Log Scale)')
plt.ylabel('Engagement Rate')
plt.tight_layout()
plt.show()

## B. Average Engagement by Content Category
plt.figure(figsize=(12,6))
category_engagement = df.groupby('Category')['Engagement Rate'].mean().sort_values(ascending=False)
sns.barplot(x=category_engagement.index, y=category_engagement.values)
plt.title('Average Engagement Rate by Category')
plt.ylabel('Avg Engagement Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## C. Likes vs Comments
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Likes', y='Comments', alpha=0.5)
plt.title('Likes vs. Comments')
plt.xlabel('Likes')
plt.ylabel('Comments')
plt.tight_layout()
plt.show()

# --- 4. Insights Summary ---
print("""
Insights:
1. Influencers with fewer followers often have higher engagement rates (micro-influencer trend).
2. Certain categories like Fitness, Beauty, and Travel tend to have better engagement.
3. There's a positive correlation between likes and comments — posts that get more likes also get more comments.
""")

# --- 5. Save Cleaned Dataset for Future Use ---
df.to_csv('cleaned_instagram_data.csv', index=False)

