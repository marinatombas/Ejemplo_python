from config import DataReader, base_path
import pandas as pd
import numpy as np
import pandas_utils
from typing import List


def clean_df(df_titles: pd.DataFrame) -> pd.DataFrame:
    """
    Function that cleans df, drops duplicates
    :param df_titles: Df we want to clean, used for the titles of films dataframe
    :return: Df without rows that contain na and without duplicates
    """
    df_cleaned = df_titles.drop_duplicates()
    return df_cleaned


def calculate_score(row: pd.Series) -> pd.Series:
    """
    Calculates the mean of imbd_score and tmdb_score
    :param row: row that we want to calculate the score from
    :return: score of the row
    """
    imdb_score = row['imdb_score']
    tmdb_score = row['tmdb_score']

    if pd.isna(imdb_score) and pd.isna(tmdb_score):
        return np.nan
    elif pd.isna(imdb_score):
        return  tmdb_score
    elif pd.isna( tmdb_score):
        return imdb_score
    else:
        return (imdb_score +  tmdb_score) / 2


def rank(df_titles_cleaned: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a df with the mean score of each movie
    :param df_titles_cleaned: df already cleaned we want to calculate scores of
    :return: a new df with columns id, title and score
    """
    df_titles_cleaned = df_titles_cleaned.copy()
    df_titles_cleaned.loc[:, 'score'] = df_titles_cleaned.apply(calculate_score, axis=1)
    df_ranked = df_titles_cleaned[['id', 'title', 'score']]
    return df_ranked


def select_directors(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Function used to select directors from a list of df
    :param dataframes:list of all the dataframes
    :return: a df where all the rows have the role Director
    """
    df = pandas_utils.filter_dfs(dataframes, 'person_id')
    df = pandas_utils.concat_df(df)
    directors_df = pandas_utils.select_values_from_column(df, 'role', 'DIRECTOR')
    return directors_df


def join(df_ranked: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the name of the directors from other df
    and joins the ranked df with the names of directors
    :param df_ranked: Df of titles already ranked
    :return: original df_ranked joined with the column name as director
    """
    dr = DataReader(base_path)
    dr.read_all_files()
    credits_df = dr.table_dict["credits.csv"]
    credits_df2 = dr.table_dict["credits2.csv"]
    credits_dfs = [credits_df.df, credits_df2.df]
    df_name = select_directors(credits_dfs).drop_duplicates()[['id', 'name']]
    df_movies_directors = df_ranked.merge(df_name, on='id', how='left')
    df_movies_directors = df_movies_directors.rename(columns={'name': 'director'})
    return df_movies_directors
