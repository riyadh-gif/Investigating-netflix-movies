# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("netflix_data.csv")

netflix_subset = netflix_df.loc[netflix_df['type'] == "Movie"]

list_id = ["title", "country", "genre", "release_year", "duration"]
netflix_movies = netflix_subset[list_id]

short_movies = netflix_movies[netflix_movies['duration'] < 60]  # Filter for movies shorter than 60 minutes

colors = []  # Initialize the colors list

for lab, row in netflix_movies.iterrows():
    if row['genre'] == "Children":
        colors.append('yellow')
    elif row['genre'] == "Documentaries":
        colors.append("gray")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

colors[:10]
fig = plt.figure(figsize=(12, 8))  
plt.title("Movie Duration by Year of Release")
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors) 
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

plt.show() 




# Display the answer
answer = "maybe"
print("Are we certain that movies are getting shorter?")
print(answer)
