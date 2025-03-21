import pandas as pd
import pandas_utils


class MostPopular:


    def __init__(self, top_n: int = 5):
        self._filename_base = '{role}_df'
        self._topn = top_n


    def most_popular(self, df_credits: pd.DataFrame) -> None:
        """
        Uses functions to calculate the self.topn most common actors and 5 most
        common directors and prints it and also saves it in new df popular_actors and
        popular_directors
        :return:
        """
        # clean df:
        clean_credits = self._clean_credits(df_credits)

        # separate actors and directors in diferent df
        actors_df = pandas_utils.select_values_from_column(clean_credits, 'role', 'ACTOR')
        directors_df = pandas_utils.select_values_from_column(clean_credits, 'role', 'DIRECTOR')

        # process and save
        self._process_and_save(actors_df, 'actors')
        self._process_and_save(directors_df, 'directors')


    def _clean_credits(self, df_credits: pd.DataFrame) -> pd.DataFrame:
        """
        Function that cleans a df, drops duplicates and NaN (except column character) as
        directors have as character value NaN, and we want to keep them
        :param df_credits: Df which contain concatenated df with the column person_id we want to clean
        :return: Df without rows that contain na and without duplicates
        """

        df_cleaned = df_credits.dropna(how='any', subset=[col for col in df_credits.columns if col != "character"])
        df_cleaned = df_cleaned.drop_duplicates()
        return df_cleaned


    def _id_count(self, df_credits_cleaned: pd.DataFrame) -> pd.DataFrame:
        """
        Given a df counts how many times an id appears
        :param df_credits_cleaned: the df which contain concatenated df with the
        column person_id already cleaned
        :return: A df with the columns person_id, count and name
        """
        count_id = df_credits_cleaned['person_id'].value_counts().reset_index()
        count_final = count_id.merge(df_credits_cleaned[['person_id', 'name']]
                                     .drop_duplicates(), on='person_id', how='left')
        return count_final


    def _process_and_save(self, df_roles: pd.DataFrame, role: str) -> None:
        """
        Processes a dataframe to get the most common roles (actors or directors),
        prints the top 5, and saves it to a CSV file.
        :param df_roles:Df we want to analyze the popularity, actors_df/directors_df
        :param role: actor/director
        """
        filename = self._filename_base.format(role=role)
        popular_df = self._id_count(df_roles)
        print(f'These are the {self._topn} most popular {role}s:\n{popular_df.head(self._topn)}')
        pandas_utils.save_df_csv(popular_df, filename)
