
def clean_credits(df_credits):
    """
    Function that cleans a df, drops duplicates and NaN (except column character) as
    directors have as character value NaN, and we want to keep them
    :param df_credits: Df which contain concatenated df with the column person_id we want to clean
    :return: Df without rows that contain na and without duplicates
    """

    df_cleaned = df_credits.dropna(how='any', subset=[col for col in df_credits.columns if col != "character"])
    df_cleaned = df_cleaned.drop_duplicates()
    return df_cleaned


def id_count(df_credits_cleaned):
    """
    Given a df counts how many times an id appears
    :param df_credits_cleaned: the df which contain concatenated df with the
    column person_id already cleaned
    :return: A df with the columns person_id, count and name
    """
    count_id = df_credits_cleaned['person_id'].value_counts().reset_index()
    count_final = count_id.merge(df_credits_cleaned[['person_id', 'name']].drop_duplicates(), on='person_id', how='left')
    return count_final




