
import media
import fresh_tomatoes

"""Gives information about the movie Toy Story to send to the Movie class"""
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",  # NOQA
    "https://www.youtube.com/watch?time_continue=78&v=v-PjgYDrg70")

"""Gives information about the movie Avatar to send to the Movie class"""
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://www.freemovieposters.net/posters/avatar_2009_2681_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?time_continue=1&v=5PSNL1qE6VY")

"""Gives information about the the Dark Knight to send to the Movie class"""
dark_knight = media.Movie(
    "The Dark Knight",
    "Batman takes on the Joker",
    "http://host.trivialbeing.org/up/tdk-new-dark-knight-poster-hi-res201949id1.jpg",  # NOQA
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

"""Gives information about the Simpsons Movie to send to the Movie class"""
simpsons = media.Movie(
    "The Simpsons Movie",
    "Simpsons appear on the movie screen when their city is threatened",
    "http://cdn2-www.comingsoon.net/assets/uploads/2007/06/file_21156_0_simpsonsnewposter2.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6W7PQpTTpec")

"""Gives information about the movie Ratatouille to send to the Movie class"""
ratatouille = media.Movie(
    "Ratatouille",
    "a rat is a chef in Paris",
    "http://au.movieposter.com/posters/archive/main/50/MPW-25274",  # NOQA
    "https://www.youtube.com/watch?v=uVeNEbh3A4U")

"""Gives information about the movie Matrix to send to the Movie class"""
matrix = media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature "
    "of his reality and his role in the war against its controllers.",
    "http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=AKrUcyBiwNw")

"""Gives information about the movie Hunger Games to send to the Movie class"""
hunger_games = media.Movie(
    "The Hunger Games",
    "A really real reality show",
    "http://cdn.collider.com/wp-content/uploads/the-hunger-games-poster1.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LrXIG4oK7Ew")


movies = [
    toy_story,
    avatar,
    dark_knight,
    simpsons,
    ratatouille,
    matrix,
    hunger_games]

fresh_tomatoes.open_movies_page(movies)
