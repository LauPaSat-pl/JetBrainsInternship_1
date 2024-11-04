"""
Here's the reference solution for the Data Processing exercise. Please note that there are multiple ways to solve this problem. The following solution is just one way to do it.

Try to solve the problem on your own before taking a look at the solution. If you are stuck, the solution can help you get back on track, but do not rely on it. Use it as a reference and try to understand each step of the solution. Don't look at other functions in the solution until you've given it a good try yourself.
"""

import pandas as pd
from pandas.core.series import Series


def load_data(path: str) -> pd.DataFrame:
    """
    Load the data from the given path and return a pandas DataFrame.
    """
    df = pd.read_csv(path)
    return df


def remove_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the columns from the DataFrame and return the modified DataFrame.
    """
    df = df[['platform', 'genre']]
    return df


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the data
    """
    df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
    return df


def group_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group the data
    """
    df = df.value_counts().unstack()
    df = df.fillna(0)
    df = df.astype(int)
    df = df.T
    return df


def save_data(df: pd.DataFrame, path: str) -> None:
    """
    Save the data to the given path
    """
    df.to_csv(path)


if __name__ == '__main__':
    df = load_data('Data source\dataset.csv')
    df = remove_columns(df)
    df = filter_data(df)
    grouped_data = group_data(df)
    save_data(grouped_data, 'Data source\processed_data.csv')
