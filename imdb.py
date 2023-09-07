import pandas as pd
from bs4 import BeautifulSoup as bs
import re
import csv
import requests
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

matplotlib.use("TkAgg")

URL = [
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=1&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=2&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=3&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=4&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=5&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=6&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=7&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=8&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=9&sort=user_rating,desc",
    "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=10&sort=user_rating,desc",
]

movies = []
ratings = []
genres = []
gross = []
runtime = []
year_of_release = []
x = []
y = []

for i in range(0, 10):
    page = requests.get(URL[i])
    soup = bs(page.content, "html.parser")

    # scraping each movie
    raw_movies = soup.find_all("h3", class_="lister-item-header")
    for movie in raw_movies:
        movie = movie.get_text().replace("\n", "")
        movie = movie.strip(" ")
        movie = movie[:-6]
        movies.append(movie)

    # scraping the ratings of each movie
    raw_ratings = soup.find_all("div", class_="ipl-rating-star small")
    for r in raw_ratings:
        r = r.get_text().replace("\n", "")
        r = r.strip(" ")
        ratings.append(r)

    # scraping the genre of each movies
    raw_genres = soup.find_all("span", class_="genre")
    for g in raw_genres:
        g = g.get_text().replace("\n", "")
        g = g.strip(" ")
        genres.append(g)

    # scraping the gross income of these movies
    raw_gross = soup.find_all("b")
    for gr in raw_gross:
        gr = gr.get_text().replace("\n", "")
        gr = gr.strip(" ")
        gr = gr[:-2]
        gross.append(gr)
    gross = gross[2:]

    # scraping the runtime of each movie
    raw_runtime = soup.find_all("span", class_="runtime")
    for run in raw_runtime:
        run = run.get_text().replace("\n", "")
        run = run.strip(" ")
        run = run.strip(" min")
        runtime.append(run)

    # scraping the Year of Release of each movie
    raw_year = soup.find_all("span", class_="lister-item-year text-muted unbold")
    for year in raw_year:
        year = year.get_text().replace("\n", "")
        year = year.replace("(", "")
        year = year.replace(")", "")
        year = year.replace("I", "")
        year = year.strip(" ")
        year_of_release.append(year)


# storing this data in a csv file
data = pd.DataFrame()
data["Movies"] = movies
data["IMDB Rating"] = ratings
data["Genre"] = genres
data["Runtime (in min)"] = runtime
data["Year of Release"] = year_of_release
data["Gross Income (in $)"] = gross
data.head()
data.to_csv("imdb.csv", index=False)


data = pd.read_csv("imdb.csv")

# for plotting genres against frequency
genre_dict = {}
for row in data["Genre"]:
    genre_list = row.split(",")
    for genre in genre_list:
        stripped_genre = genre.strip()
        if stripped_genre in genre_dict:
            genre_dict[stripped_genre] += 1
        else:
            genre_dict[stripped_genre] = 1

genre_counts = pd.Series(genre_dict)
plt.bar(genre_counts.index, genre_counts.values)
plt.xticks(rotation=90)
plt.xlabel("Genre")
plt.ylabel("Frequency")
plt.title("Frequency of movies by genre")
plt.show()

# for plotting gross value against movies
gross_values = []
for gross in gross:
    gross = gross.replace("$", "").replace(",", "")
    gross_values.append(float(gross))
gross_values = data["Gross Income (in $)"]

gross_values = data["Gross Income (in $)"].apply(lambda x: re.sub("[^0-9]", "", str(x)))
gross_movies = data["Movies"]
gross_values = gross_values.astype(float)
gross_top100 = (
    pd.DataFrame({"Gross Income (in $)": gross_values, "Movies": gross_movies})
    .sort_values(by=["Gross Income (in $)"], ascending=False)
    .head(100)
)
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(gross_top100["Movies"], gross_top100["Gross Income (in $)"])
fmt = "${x:,.0f}00M"
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

plt.xlabel("Date", fontsize=14)
plt.ylabel("Gross Value (Hundreds of Millions)", fontsize=14)
plt.title("Gross Value of Movies over Time", fontsize=16)

plt.xticks(fontsize=12, rotation=90)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()
