"""

Visualization module for the SO challenge.

This module handles plotting and visualizing data.

"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_questions(df):
    """
    Plot monthly question counts with a 12-month rolling average.

    Args:
        df (pd.DataFrame): DataFrame with columns 'year_month' and 'question_count'.
    """
    # Ensure the DataFrame has the required columns
    if not {'year_month', 'question_count'}.issubset(df.columns):
        raise ValueError("DataFrame must contain 'year_month' and 'question_count' columns")

    # Plot monthly question counts
    plt.plot(df['year_month'], df['question_count'], color='blue', label='Monthly Questions')

    # Calculate and plot 12-month rolling average
    rolling_avg = df['question_count'].rolling(window=12).mean()
    plt.plot(df['year_month'], rolling_avg, color='red', label='12-Month Rolling Average')

    # Label axes
    plt.xlabel('Month')
    plt.ylabel('Questions')

    # Show the plot
    plt.show()