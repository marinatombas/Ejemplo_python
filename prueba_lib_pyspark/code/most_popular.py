import pandas as pd
import pandas_utils


def clean_credits(df_credits: pd.DataFrame) -> pd.DataFrame:
    """
    Function that cleans a df, drops duplicates and NaN (except column character) as
    directors have as character value NaN, and we want to keep them
    :param df_credits: Df which contain concatenated df with the column person_id we want to clean
    :return: Df without rows that contain na and without duplicates
    """

    df_cleaned = df_credits.dropna(how='any', subset=[col for col in df_credits.columns if col != "character"])
    df_cleaned = df_cleaned.drop_duplicates()
    return df_cleaned


def id_count(df_credits_cleaned: pd.DataFrame) -> pd.DataFrame:
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


def process_and_save(df_roles: pd.DataFrame, role: str) -> None:
    """
    Processes a dataframe to get the most common roles (actors or directors),
    prints the top 5, and saves it to a CSV file.
    :param df_roles:Df we want to analyze the popularity, actors_df/directors_df
    :param role: actor/director
    """
    filename = f'{role}_df'
    popular_df = id_count(df_roles)
    print(f'These are the 5 most popular {role}s:\n{popular_df.head(5)}')
    pandas_utils.save_df_csv(popular_df, filename)
