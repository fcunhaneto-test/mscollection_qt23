#!/home/francisco/Projects/Pycharm/mscollection_qt23/venv/bin/python
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QMdiArea, QMenu, QMenuBar, \
    QStatusBar, QAction, QDesktopWidget, QApplication

import texts

# Inserts
from subwindows.insert.insert_movie import InsertMovie
from subwindows.insert.insert_series import InsertSeries
from subwindows.insert.insert_season import InsertSeason

# Edits
from subwindows.edit.edit_movie import EditMovie
from subwindows.edit.edit_series import EditSeries
from subwindows.edit.edit_season import EditSeason

from subwindows.edit.edit_cast import EditCast
from subwindows.edit.edit_director import EditDirector
from subwindows.edit.edit_creator import EditCreator
from subwindows.edit.edit_others import EditOthers

from subwindows.edit.edit_season_cast import EditSeasonCast

from rewrite_html.rewrite_html import RewriteHtml

# Searchs
from subwindows.search.search_movie_title import SearchMovieTitle
from subwindows.search.search_series_title import SearchSeriesTitle
from subwindows.search.search_movie_box import SearchMovieBox

from subwindows.search.search_ms_category import SearchMSCategory
from subwindows.search.search_ms_keyword import SearchMSKeyword
from subwindows.search.search_ms_media_year import SearchMSMediaYear


from subwindows.search.view_select_title import ViewSelectTitle
from subwindows.search.view_movie_web_url import ViewMovieUrl
from subwindows.search.view_series_web_url import ViewSeriesUrl
from subwindows.search.view_movie_search_url import  ViewMovieSearchUrl
from subwindows.search.view_series_search_url import  ViewSeriesSearchUrl


class MSCollection(QMainWindow):
    """
    Class of the main window and that also manages the display of all other
    windows.
    """
    def __init__(self):
        super(MSCollection, self).__init__()

        css = 'styles/style.qss'
        with open(css, 'r') as fh:
            self.setStyleSheet(fh.read())

        self.setWindowTitle(texts.main_widow)
        screen = QDesktopWidget().screenGeometry()
        s_width = screen.width()
        s_heigth = screen.height()
        x = int(0.10 * s_width)
        y = int(0.10 * s_heigth)
        width = int(0.8 * s_width)
        height = int(0.8 * s_heigth)

        self.setGeometry(x, y, width, height)

        self.mdi_area = QMdiArea()
        brush = QBrush(QColor(250, 248, 224))
        brush.setStyle(Qt.SolidPattern)
        self.mdi_area.setBackground(brush)

        self.setCentralWidget(self.mdi_area)
        self.menubar = QMenuBar(self)

        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        # Menu and Submenu
        self.menu_insert = QMenu(self.menubar)
        self.menu_insert.setTitle(texts.insert)

        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setTitle(texts.edit)
        self.menu_edit_movie_others = QMenu(self.menu_edit)
        self.menu_edit_movie_others.setTitle(texts.menu_movie_others)
        self.menu_edit_series_others = QMenu(self.menu_edit)
        self.menu_edit_series_others.setTitle(texts.menu_series_others)
        self.menu_edit_season = QMenu(self.menu_edit)
        self.menu_edit_season.setTitle(texts.season_p)
        self.menu_edit_general = QMenu(self.menu_insert)
        self.menu_edit_general.setTitle(texts.general)
        self.menu_delete_orphans = QMenu(texts.delete_orphans)

        self.menu_search = QMenu(self.menubar)
        self.menu_search.setTitle(texts.search)
        self.menu_search_movies = QMenu(self.menu_search)
        self.menu_search_movies.setTitle(texts.movie_p)
        self.menu_search_series = QMenu(self.menu_search)
        self.menu_search_series.setTitle(texts.series_p)

        # Actions Insert ######################################################
        self.action_insert_movie = QAction(
            texts.movie_p, self, triggered=self.insert_movie)
        self.action_insert_series = QAction(
            texts.series_p, self, triggered=self.insert_series)
        self.action_insert_season = QAction(
            texts.season_p, self, triggered=self.insert_season)

        # AddAction Insert
        self.menu_insert.addAction(self.action_insert_movie)
        self.menu_insert.addAction(self.action_insert_series)
        self.menu_insert.addAction(self.action_insert_season)

        # Actions Edit ######################################################
        self.action_edit_movie = QAction(
            texts.movie_p, self, triggered=self.edit_movie)
        self.action_edit_series = QAction(
            texts.series_p, self, triggered=self.edit_series)
        self.action_edit_season = QAction(
            texts.season_p, self, triggered=self.edit_season)
        self.action_edit_rewrite_html = QAction(
            texts.rewrite_html, self, triggered=self.rewrite_html)

        self.action_edit_movie_cast = QAction(
            texts.cast_s, self, triggered=self.edit_movie_cast)
        self.action_edit_series_cast = QAction(
            texts.cast_s, self, triggered=self.edit_series_cast)

        self.action_edit_director = QAction(texts.director_s, self,
                                            triggered=self.edit_director)
        self.action_edit_creator = QAction(texts.creator_s, self,
                                           triggered=self.edit_creator)

        self.action_edit_box = QAction(texts.box, self)
        self.action_edit_box.triggered.connect(lambda: self.edit_others('box'))
        self.action_edit_category = QAction(texts.category_p, self)
        self.action_edit_category.triggered.connect(
            lambda: self.edit_others('category'))
        self.action_edit_media = QAction(texts.media_s, self)
        self.action_edit_media.triggered.connect(
            lambda: self.edit_others('media'))
        self.action_edit_actor = QAction(texts.actor_s, self)
        self.action_edit_actor.triggered.connect(
            lambda: self.edit_others('actor'))
        self.action_edit_character = QAction(texts.character_s, self)
        self.action_edit_character.triggered.connect(
            lambda: self.edit_others('character'))
        self.action_edit_keyword = QAction(texts.keyword, self)
        self.action_edit_keyword.triggered.connect(
            lambda: self.edit_others('keyword'))

        text = texts.season_s + ' ' + texts.cast_s
        self.action_edit_season_cast = QAction(
            text, self, triggered=self.edit_season_cast)

        # AddAction Edit
        self.menu_edit.addAction(self.action_edit_movie)
        self.menu_edit.addAction(self.menu_edit_movie_others.menuAction())
        self.menu_edit_movie_others.addAction(self.action_edit_movie_cast)
        self.menu_edit_movie_others.addAction(self.action_edit_director)
        self.menu_edit_movie_others.addAction(self.action_edit_box)

        self.menu_edit.addAction(self.action_edit_series)
        self.menu_edit.addAction(self.menu_edit_series_others.menuAction())
        self.menu_edit_series_others.addAction(self.action_edit_series_cast)
        self.menu_edit_series_others.addAction(self.action_edit_creator)

        self.menu_edit.addAction(self.menu_edit_general.menuAction())
        self.menu_edit_general.addAction(self.action_edit_category)
        self.menu_edit_general.addAction(self.action_edit_media)
        self.menu_edit_general.addAction(self.action_edit_actor)
        self.menu_edit_general.addAction(self.action_edit_character)
        self.menu_edit_general.addAction(self.action_edit_keyword)

        self.menu_edit.addAction(self.action_edit_season)
        self.menu_edit.addAction(self.action_edit_season_cast)
        self.menu_edit.addAction(self.action_edit_rewrite_html)

        # Actions Search ######################################################
        self.actions_search_movie_title = QAction(
            texts.title_s, self, triggered=self.search_movie_title)
        self.actions_view_movie_web_url = QAction(
            texts.lb_url, self, triggered=self.view_movie_web_url)
        self.actions_search_series_title = QAction(
            texts.title_s, self, triggered=self.search_series_title)
        self.actions_search_movie_box = QAction(
            texts.box, self, triggered=self.search_movie_box)
        self.actions_search_movie_category = QAction(texts.category_p, self)
        self.actions_search_movie_category.triggered.connect(
            lambda: self.search_ms_category('movie'))
        self.actions_search_series_category = QAction(texts.category_p, self)
        self.actions_search_series_category.triggered.connect(
            lambda: self.search_ms_category('series'))
        self.actions_search_movie_keyword = QAction(texts.keyword, self)
        self.actions_search_movie_keyword.triggered.connect(
            lambda: self.search_ms_keyword('movie'))
        self.actions_search_series_keyword = QAction(texts.keyword, self)
        self.actions_search_series_keyword.triggered.connect(
            lambda: self.search_ms_keyword('series'))
        text = texts.media_s + '/' + texts.year_s
        self.actions_search_movie_my = QAction(text, self)
        self.actions_search_movie_my.triggered.connect(
            lambda: self.search_ms_my('movie'))
        self.actions_search_series_my = QAction(text, self)
        self.actions_search_series_my.triggered.connect(
            lambda: self.search_ms_my('series'))

        self.actions_view_series_web_url = QAction(
            texts.lb_url, self, triggered=self.view_series_web_url)


        # AddAction Search
        self.menu_search_movies.addAction(self.actions_search_movie_title)
        self.menu_search_movies.addAction(self.actions_search_movie_box)
        self.menu_search_movies.addAction(self.actions_search_movie_category)
        self.menu_search_movies.addAction(self.actions_search_movie_keyword)
        self.menu_search_movies.addAction(self.actions_search_movie_my)


        self.menu_search_series.addAction(self.actions_search_series_title)
        self.menu_search_series.addAction(self.actions_search_series_category)
        self.menu_search_series.addAction(self.actions_search_series_keyword)
        self.menu_search_series.addAction(self.actions_search_series_my)


        self.menu_search.addAction(self.menu_search_movies.menuAction())
        self.menu_search.addAction(self.menu_search_series.menuAction())

        # AddAction Menu ######################################################
        self.menubar.addAction(self.menu_insert.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_search.menuAction())

    """
    All methods below is for open subwindows
    """
    def insert_movie(self):
        subwindow = InsertMovie(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def insert_series(self):
        subwindow = InsertSeries(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def insert_season(self):
        subwindow = InsertSeason(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_movie(self):
        subwindow = EditMovie(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_series(self):
        subwindow = EditSeries(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_season(self):
        subwindow = EditSeason(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def rewrite_html(self):
        subwindow = RewriteHtml(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_movie_cast(self):
        subwindow = EditCast(self, 'movie')
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_series_cast(self):
        subwindow = EditCast(self, 'series')
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_season_cast(self):
        subwindow = EditSeasonCast(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_director(self):
        subwindow = EditDirector(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_creator(self):
        subwindow = EditCreator(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def edit_others(self, op):
        subwindow = EditOthers(self, op)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def view_html(self, url, title):
        subwindow = ViewSelectTitle(self, url, title)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def search_movie_title(self):
        subwindow = SearchMovieTitle(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def search_series_title(self):
        subwindow = SearchSeriesTitle(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def search_movie_box(self, type):
        subwindow = SearchMovieBox(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def search_ms_category(self, type):
        subwindow = SearchMSCategory(self, type)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def search_ms_keyword(self, type):
        subwindow = SearchMSKeyword(self, type)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def search_ms_my(self, type):
        subwindow = SearchMSMediaYear(self, type)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def view_movie_web_url(self):
        subwindow = ViewMovieUrl(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def view_series_web_url(self):
        subwindow = ViewSeriesUrl(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def view_movie_search_url(self):
        subwindow = ViewMovieSearchUrl(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def view_series_search_url(self):
        subwindow = ViewSeriesSearchUrl(self)
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MSCollection()
    main_window.show()
    sys.exit(app.exec_())