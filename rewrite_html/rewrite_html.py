from rewrite_html.db_model_no_widgets import Movie

from rewrite_html.db_settings_no_wiget import Database

from rewrite_html.rewrite_movies_html import write_movie_html

session = Database.get_session()

movies = session.query(Movie).all()

for m in movies:
    view = write_movie_html(session, m)
    m.view = view
    session.commit()