import pandas as pd
import os
import config

def concat_df(df_list):
    """
    Concat the df
    :param df_list: Enter the desired list of df
    :return: concated df
    """
    if not df_list:  # Check if the list is empty
        print("There is no object in the list to concatenate")
    else:
        df_final = pd.concat(df_list, ignore_index=True)
        return df_final

def filter_dfs(df_list,*args):
    """
    selects df that have determined column names
    :param df_list: List of dfs
    :param args: List of columns that must appear in the df
    :return: list of df that have the columns you list in *args
    """
    if not df_list:  # Check if the list is empty
        print("There is no object in the list to concatenate")
    else:
        desired_columns = set(args)
        dfs_filtered = [df for df in df_list if desired_columns.issubset(df.columns)]
        return dfs_filtered


def select_values_from_column(df, column_name, target_value):
    """
    Selects rows from a DataFrame where a specified column has a target value
    :param df: The pandas DataFrame to filter
    :param column_name: The name of the column to check
    :param target_value: The value to filter for in the specified column
    :return: A DataFrame containing only the rows where the column has the target value
    """
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in DataFrame.")

    try:
        selected_rows = df[df[column_name] == target_value]
        return selected_rows
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

def save_df_csv(df_to_save, df_name, route=config.save_files, separator=","):
    """
    saves the desired df in a csv
    :param df_to_save: the df we want to save
    :param df_name: name of the saved file
    :param route: where we want to save it, default in folder files
    :param separator: what separates the data, default ','
    :return: nothing
    """
    full_route = os.path.join(route, f"{df_name}.csv")
    try:
     df_to_save.to_csv(full_route, sep=separator, index=False)
     print(f"Files saved successfully in '{full_route}'")
    except Exception as e:
     print(f"Error while saving the file in '{full_route}': {e}")

