from user import User
from admin import Admin
from movie import Movie
from subscirption import Subscription

movie1 = Movie(1, "Bad Boys for Life", "Action", 2020, 9.8)
movie2 = Movie(2, "Joker", "Drama", 2019, 10)
movie3 = Movie(3, "Jackass Forever", "Comedy", 2022, 9)

user1 = User(1, "viktorviktorov99", "viktor99@gmail.com")
user2 = User(2, "rosenrosenov97", "rosen97@icloud.com")

user1.add_movie_to_favorites(movie1)
user1.add_movie_to_favorites(movie2)
user1.add_movie_to_favorites(movie3)

recommendations = user1.get_recommendations()
print("User1's Recommendations:", [movie.title for movie in recommendations])

user2.add_movie_to_favorites(movie2)
user2.mark_movie_as_watched(movie2)
print(user2.rate_movie(movie2, 5))

watched_movies = user2.get_watched_movies()
print("User2's Watched Movies:", [movie.title for movie in watched_movies])

admin = Admin(1, "Admin1")
admin.add_movie(Movie(4, "Azor", "Thriller", 2021, 9.8))
admin.remove_movie(movie2)

print("Movie Information:")
print(movie1.get_info())

subscription1 = Subscription(1, "Basic", 10, 7)
subscription2 = Subscription(2, "Premium", 15, 14)
user1.subscribe(subscription1)
user2.subscribe(subscription2)

print("Subscription Information:")
print(subscription1.get_info())


