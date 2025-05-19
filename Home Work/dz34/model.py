import pickle
import os.path


class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"


class MovieModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.movies = self.load_data()

    def add_movie(self, dict_movies):
        movie = Movie(*dict_movies.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, user_movie):
        movie = self.movies[user_movie]
        dict_movie = {
            "название": movie.title,
            "жанр": movie.genre,
            "режиссер": movie.director,
            "год": movie.year,
            "длительность": movie.duration,
            "студия": movie.studio,
            "актеры": movie.actors
        }
        return dict_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.movies, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
