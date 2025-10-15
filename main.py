import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("movies.csv")
print("🎬 Movie Dataset Loaded!\n")

# Explore the data
print(df.head(), "\n")
print("Dataset Info:\n")
print(df.info(), "\n")
print("Summary Stats:\n", df.describe(), "\n")

# Clean the data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Add a new column for 'decade'
df["decade"] = (df["year"] // 10 * 10).astype(str) + "s"

# Filter movies with rating above 8.5
high_rated = df[df["rating"] > 8.5]
print("Top Rated Movies:\n", high_rated[["title", "rating"]], "\n")

# Group by genre average rating
avg_by_genre = df.groupby(
    "genre")["rating"].mean().sort_values(ascending=False)
print("Average Rating by Genre:\n", avg_by_genre, "\n")

# Group by decade average rating
avg_by_decade = df.groupby("decade")["rating"].mean()
print("Average Rating by Decade:\n", avg_by_decade, "\n")

# Visualization Genre Ratings
avg_by_genre.plot(kind="bar", title="Average Rating by Genre")
plt.ylabel("Average Rating")
plt.show()

# Visualization Decade Ratings
avg_by_decade.plot(kind="line", marker="o", title="Average Rating by Decade")
plt.ylabel("Average Rating")
plt.show()

# Save cleaned dataset
df.to_csv("cleaned_movies.csv", index=False)
print("Cleaned data saved to cleaned_movies.csv")
