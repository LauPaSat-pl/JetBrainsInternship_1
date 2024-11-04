"""
Here's the reference solution for the Data Processing exercise. Please note that there are multiple ways to solve this problem. The following solution is just one way to do it.

Try to solve the problem on your own before taking a look at the solution. If you are stuck, the solution can help you get back on track, but do not rely on it. Use it as a reference and try to understand each step of the solution. Don't look at other functions in the solution until you've given it a good try yourself.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """
    Load the data from the given path and return a pandas DataFrame.
    """
    df = pd.read_csv(path)
    df = df.set_index('genre')
    df = df[['PS4', 'XOne', 'PC', 'WiiU']]
    return df


def plot_data(df: pd.DataFrame) -> None:
    """
    Plot the data
    """
    # Extract the labels
    platforms = df.columns
    genres = df.index

    # Create the figure and set the size
    plt.figure(figsize=(20, 10))
    x = np.arange(len(platforms))
    width = 0.05

    # Create the bars for each genre. Each genre will have a different color.
    # We loop over the genres and create a bar for each genre on any platform.
    for i, genre in enumerate(genres):
        plt.bar(x + i * width, df.loc[genre], width=width, label=genre)

    # Set the x-axis ticks and labels
    plt.xticks(x + 5 * width, platforms)

    # Add labels and title
    plt.xlabel('Platform')
    plt.ylabel('Count')
    plt.title('Game Count by Genre and Platform')

    # Add legend
    plt.legend()

    # Save the plot
    plt.savefig('final_plot_example.png')


if __name__ == '__main__':
    df = load_data('Data source\processed_data.csv')
    df = plot_data(df)
