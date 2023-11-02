class User:
    def __init__(self, user_id, username, email):
        self.__user_id = user_id
        self._username = username
        self._email = email
        self.__favorite_movies = []
        self.__watched_movies = []

    def add_movie_to_favorites(self, movie):
        self.__favorite_movies.append(movie)

    def get_recommendations(self):
        return self.__favorite_movies[-3:]

    def mark_movie_as_watched(self, movie):
        if movie in self.__favorite_movies:
            self.__favorite_movies.remove(movie)
            self.__watched_movies.append(movie)

    def rate_movie(self, movie, rating):
        if 1 <= rating <= 5:
            movie.rating = rating
        return f'User: "{self._username}" rated this movies with {rating} stars.'

    def get_watched_movies(self):
        return self.__watched_movies

    def subscribe(self, subscription):
        self.subscription = subscription
