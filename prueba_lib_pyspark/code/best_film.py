import config
import pandas as pd
import numpy as np
import read_prepare_save


def clean_df(df_titles):
    """
    Function that cleans df, drops duplicates
    :param df_titles: Df we want to clean, used for the titles of films dataframe
    :return: Df without rows that contain na and without duplicates
    """
    df_cleaned = df_titles.drop_duplicates()
    return df_cleaned


def calculate_score(row):
    """
    Calculates the mean of imbd_score and tmdb_score
    :param row: row that we want to calculate the score from
    :return: score of the row
    """
    if pd.isna(row['imdb_score']) and pd.isna(row['tmdb_score']):
        return np.nan
    elif pd.isna(row['imdb_score']):
        return row['tmdb_score']
    elif pd.isna(row['tmdb_score']):
        return row['imdb_score']
    else:
        return (row['imdb_score'] + row['tmdb_score']) / 2


def rank(df_titles_cleaned):
    """
    Creates a df with the mean score of each movie
    :param df_titles_cleaned: df already cleaned we want to calculate scores of
    :return: a new df with columns id, title and score
    """
    df_titles_cleaned = df_titles_cleaned.copy()
    df_titles_cleaned.loc[:, 'score'] = df_titles_cleaned.apply(calculate_score, axis=1)
    df_ranked = df_titles_cleaned[['id', 'title', 'score']]
    return df_ranked


def select_directors(dataframes):
    """
    Function used to select directors from a list of df
    :param dataframes:list of all the dataframes
    :return: a df where all the rows have the role Director
    """
    df = read_prepare_save.filter_dfs(dataframes, 'person_id')
    df = read_prepare_save.concat_df(df)
    directors_df = read_prepare_save.select_values_from_column(df, 'role', 'DIRECTOR')
    return directors_df


def join(df_ranked):
    """
    Takes the name of the directors from other df
    and joins the ranked df with the names of directors
    :param df_ranked: Df of titles already ranked
    :return: original df_ranked joined with the column name as director
    """
    df_name = select_directors(config.dfs).drop_duplicates()[['id', 'name']]
    df_movies_directors = df_ranked.merge(df_name, on='id', how='left')
    df_movies_directors = df_movies_directors.rename(columns={'name': 'director'})
    return df_movies_directors
