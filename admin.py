# class Admin:
#     def __init__(self, admin_id, username):
#         self.__admin_id = admin_id
#         self._username = username
#
#     def add_movie(self, movie):
#         pass
#
#     def remove_movie(self, movie):
#         pass

# we can implement the code here and so we can raise an exception like:
from movie import Movie
class Admin:
    def __init__(self, admin_id, username):
        self.__admin_id = admin_id
        self._username = username
        self.movies = []

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            self.movies.append(movie)

        else:
            raise ValueError("Invalid movie object. Please provide a valid movie.")

    def remove_movie(self, movie):
        if isinstance(movie, Movie):
            if movie in self.movies:
                self.movies.remove(movie)
        else:
            raise ValueError("Invalid movie object. Please provide a valid movie.")
