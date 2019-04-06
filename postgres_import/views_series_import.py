from db.db_model import Series

from db.db_settings import Database as DB

from lib.write_series_html import write_series_html

session = DB.get_session()

query = session.query(Series).all()

for series in query:
    series.view = write_series_html(session, series)
    session.add(series)
    session.commit()
