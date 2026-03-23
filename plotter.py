"""

Visualization module for the SO challenge.

This module handles plotting and visualizing data.

"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


def plot_questions(ax, df):
    """
    Plot monthly question counts with a 12-month rolling average.

    Args:
        ax: Matplotlib axes object.
        df (pd.DataFrame): DataFrame with columns 'year_month' and 'question_count'.
    """
    # Ensure the DataFrame has the required columns
    if not {'year_month', 'question_count'}.issubset(df.columns):
        raise ValueError("DataFrame must contain 'year_month' and 'question_count' columns")

    # Convert year_month to datetime
    df = df.copy()
    df['date'] = pd.to_datetime(df['year_month'] + '-01')

    # Plot monthly question counts
    ax.plot(df['date'], df['question_count'], color='blue', label='Monthly Questions')

    # Calculate and plot 12-month rolling average
    rolling_avg = df['question_count'].rolling(window=12).mean()
    ax.plot(df['date'], rolling_avg, color='red', label='12-Month Rolling Average')

    # Label axes
    ax.set_xlabel('Month')
    ax.set_ylabel('Questions')

    # Format x-axis as dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    plt.setp(ax.get_xticklabels(), rotation=45)

    # Add legend
    ax.legend()