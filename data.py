import pandas as pd
import csv

movies = pd.read_csv("imdb.csv")
top_100 = movies.sort_values(by=["IMDB Rating", "Runtime (in min)"], ascending=[False, True]).head(100)
print("The top 100 movies are\n")
print(top_100["Movies"])
with open('imdb.csv') as csvfile:
    csvfile.close()


with open('imdb.csv', 'r') as csvfile:
    movies = csv.reader(csvfile)

    next(movies)

    print("\n\n")
    print("The Filter Options are\n")
    print("1. Duration\n")
    print("2. IMDB Rating\n")
    print("3. Year of Release\n")
    print("4. Genre\n")

    option = input()

    if option == "1":
        for movie in movies:
            movie[3] = int(movie[3])

        min_dur, max_dur = input("Enter the range:\n").split()
        min_dur = int(min_dur)
        max_dur = int(max_dur)
        csvfile.seek(0)
        next(movies)

        for movie in movies:
            if int(movie[3]) > min_dur and int(movie[3]) < max_dur:
                print(movie[0])

    if option == '2':
        for movie in movies:
            movie[1] = float(movie[1])
        min_rating, max_rating = input("Enter the range:\n").split()
        min_rating = float(min_rating)
        max_rating = float(max_rating)
        csvfile.seek(0)
        next(movies)
        for movie in movies:
            if float(movie[1]) >= min_rating and float(movie[1]) <= max_rating:
                print(movie[0])

    if option == '3':
        for movie in movies:
            movie[4] = int(movie[4])

        min_year, max_year = input("Enter the range:\n").split()
        min_year = int(min_year)
        max_year = int(max_year)
        csvfile.seek(0)
        next(movies)
        for movie in movies:
            if int(movie[4]) >= min_year and int(movie[4]) <= max_year:
                print(movie[0])

    if option == '4':
        genre = input("Enter Genre:\n")
        csvfile.seek(0)
        next(movies)
        for movie in movies:
            genres_list = movie[2].split(',')
            if genre.strip() in genres_list:
                print(movie[0])


