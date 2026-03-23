#!/usr/bin/env python3
"""
Main script for the SO Challenge project.

Fetches Stack Overflow question data, plots it with a rolling average,
and overlays AI milestone markers.
"""

import matplotlib.pyplot as plt
from data_fetcher import fetch_so_data
from plotter import plot_questions
from milestones import overlay_milestones

# Define AI milestones
MILESTONES = {
    '2017-06-01': 'Transformer',
    '2022-11-01': 'ChatGPT',
    '2023-03-01': 'GPT-4',
    '2023-08-01': 'Cursor and AI IDEs',
    '2025-02-01': 'Claude Code',
    '2025-02-01': 'GitHub Copilot Agent Mode'
}

def main():
    # Fetch data
    print("Fetching Stack Overflow data...")
    df = fetch_so_data()
    print(f"Data fetched: {df.shape[0]} months")

    # Create plot
    fig, ax = plt.subplots(figsize=(12, 6))
    plot_questions(ax, df)
    overlay_milestones(ax, MILESTONES)

    # Finalize plot
    plt.title('Stack Overflow Monthly Questions with AI Milestones')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()