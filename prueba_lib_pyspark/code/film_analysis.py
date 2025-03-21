import pandas_utils
from most_popular import MostPopular
from config import DataReader
from best_film import BestFilm


class FilmAnalysis:

    def __init__(self, base_path):
        self._dr = DataReader(base_path)
        self._dr.read_all_files()


    def most_popular_actor_director(self, topn: int = 5):
        """
        Prepares data for calculating 5 most popular actors and directors.
        Acts as a wrapper for all business logic
        """
        credits_df = self._dr.table_dict["credits.csv"]
        credits_df2 = self._dr.table_dict["credits2.csv"]
        credits_dfs = [credits_df.df, credits_df2.df]
        # concat dfs
        concat_credits = pandas_utils.concat_df(credits_dfs)

        most_popular_obj = MostPopular(topn)
        most_popular_obj.most_popular(concat_credits)


    def award_best_film(self):
        # concat df
        titles_1=self._dr.table_dict["titles.csv"]

        best_film_obj = BestFilm(self._dr)
        best_film_obj.best_film(titles_1.df)

