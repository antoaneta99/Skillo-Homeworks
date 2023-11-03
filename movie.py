class Movie:
    def __init__(self, movie_id, title, genre, release_year, rating):
        self.__movie_id = movie_id
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def get_info(self):
        return (f"Movie ID: {self.__movie_id}\n"
                f"Title: {self.title}\n"
                f"Genre: {self.genre}\n"
                f"Release Year: {self.release_year}\n"
                f"Rating: {self.rating}")