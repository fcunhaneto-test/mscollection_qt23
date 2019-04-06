from db.db_model import Director, Box, Keyword, Movie, MovieDirector, MovieCast
from db.db_model import Media, Actor, Character, Category, Cast

from db.db_settings import Database as DB

from lib.write_movie_html import write_movie_html

session = DB.get_session()

movies = session.query(Movie).all()

for movie in movies:
    movie.view = write_movie_html(session, movie)
    session.add(movie)
    session.commit()
