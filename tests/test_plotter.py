"""

Tests for plotter module.

"""

import pytest
import pandas as pd
from unittest import mock
from plotter import plot_questions


class TestPlotter:
    def test_accepts_correct_dataframe(self):
        ax = mock.Mock()
        df = pd.DataFrame({
            'year_month': ['2008-01', '2008-02', '2008-03'],
            'question_count': [100, 150, 200]
        })
        plot_questions(ax, df)
        # Should not raise error
        ax.plot.assert_called()

    def test_plot_has_two_lines_correct_colors(self):
        ax = mock.Mock()
        df = pd.DataFrame({
            'year_month': ['2008-01', '2008-02', '2008-03', '2008-04', '2008-05', '2008-06',
                           '2008-07', '2008-08', '2008-09', '2008-10', '2008-11', '2008-12',
                           '2009-01'],
            'question_count': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
        })
        plot_questions(ax, df)
        # Check ax.plot calls
        calls = ax.plot.call_args_list
        assert len(calls) == 2
        # First call: blue line for monthly
        assert calls[0][1]['color'] == 'blue'
        # Second call: red line for rolling average
        assert calls[1][1]['color'] == 'red'

    def test_axes_labeled_correctly(self):
        ax = mock.Mock()
        df = pd.DataFrame({
            'year_month': ['2008-01', '2008-02'],
            'question_count': [100, 150]
        })
        plot_questions(ax, df)
        ax.set_xlabel.assert_called_with('Month')
        ax.set_ylabel.assert_called_with('Questions')

    def test_rolling_average_calculated_correctly(self):
        ax = mock.Mock()
        df = pd.DataFrame({
            'year_month': [f'2008-{i:02d}' for i in range(1, 13)] + ['2009-01'],
            'question_count': list(range(100, 113))  # 100 to 112
        })
        plot_questions(ax, df)
        calls = ax.plot.call_args_list
        # The rolling average for the last point should be the average of the last 12
        # For 13 points, rolling mean at index 12 is mean of 0 to 11
        expected_rolling = df['question_count'].rolling(12).mean().iloc[-1]
        # Check the y data for the red line
        red_line_y = calls[1][0][1]  # Second call, second arg is y
        assert red_line_y.iloc[-1] == pytest.approx(expected_rolling)