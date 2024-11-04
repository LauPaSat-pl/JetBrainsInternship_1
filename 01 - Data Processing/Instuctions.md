# Theory
## Matplotlib
Matplotlib is one of the most popular plotting libraries for Python. It is a powerful library that can be used to create a wide range of plots, graphs, and charts. Matplotlib is highly customizable and provides a wide range of options for customizing the appearance of plots, but as this is a basic course, we will only cover the simple bar chart. For more information on Matplotlib, you can refer to the official website: https://matplotlib.org/

## Data Processing
Data processing is a crucial step in data analysis and visualisation. It involves cleaning, transforming, and preparing the data for analysis. Data processing is important because it ensures that the data is accurate, consistent, and complete. In this task, you will learn how to load data from a CSV file, remove unnecessary columns, filter the data, and group the data for visualisation.

## Pandas
In this task, you will use the Pandas library to load and process the data. If you are not familiar with Pandas, you can refer to the getting started guide on the official website: https://pandas.pydata.org/docs/getting_started/index.html

# Instructions
Follow the steps below to complete the task. You should write your code in the `main.py` file and do NOT change the function signature of the functions provided in the `main.py` file as they are required for testing. If you want to test your code, you can check the reference solution in the `solution.py` file.
1. Load the data from the `data.csv` file using Pandas in 'load_data' function. The data is in CSV format.
2. Remove unnecessary columns from the data in 'remove_columns' function. Keep only the columns that are required for visualisation.
<details>
<summary><b>Columns to stay</b></summary>

platform, genre

</details>

3. Remove rows with games from other platforms in 'filter_data' function. You should keep only the rows with games for the 'PS4', 'XOne', 'PC' and 'WiiU'.
4. Group the data by appropriate columns in 'group_data' function.

Congratulations! You have successfully processed the data. Now you can move on to the next step of visualising the data.