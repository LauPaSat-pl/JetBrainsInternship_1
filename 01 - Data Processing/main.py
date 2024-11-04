"""
Write your solutions in the corresponding functions in this file.
"""

import pandas as pd
from pandas.core.series import Series


def load_data(path: str) -> pd.DataFrame:
    """
    Load the data from the given path and return a pandas DataFrame.
    """
    pass
    return df


def remove_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the columns from the DataFrame and return the modified DataFrame.
    """
    pass
    return df


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the data
    """
    pass
    return df


def group_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group the data
    """
    pass
    return grouped_data


def save_data(df: pd.DataFrame, path: str) -> None:
    """
    Save the data to the given path
    """
    df.to_csv(path, index=False)


if __name__ == '__main__':
    df = load_data('Data source\dataset.csv')
    df = remove_columns(df)
    df = filter_data(df)
    grouped_data = group_data(df)
    save_data(grouped_data, 'Data source\grouped_data.csv')
