"""

Tests for milestones module.

"""

import pytest
from unittest import mock
from milestones import overlay_milestones
import pandas as pd


class TestMilestones:
    @mock.patch('milestones.plt')
    def test_accepts_correct_input(self, mock_plt):
        axes = mock.Mock()
        milestones = {
            '2017-06': 'Transformer',
            '2022-11': 'ChatGPT'
        }
        overlay_milestones(axes, milestones)
        # Should not raise error
        axes.axvline.assert_called()

    @mock.patch('milestones.plt')
    def test_correct_placement_of_markers(self, mock_plt):
        axes = mock.Mock()
        milestones = {
            '2017-06-01': 'Transformer',
            '2022-11-01': 'ChatGPT',
            '2023-03-01': 'GPT-4'
        }
        overlay_milestones(axes, milestones)
        calls = axes.axvline.call_args_list
        # Check x positions
        expected_dates = [pd.to_datetime('2017-06-01'), pd.to_datetime('2022-11-01'), pd.to_datetime('2023-03-01')]
        for i, call in enumerate(calls):
            assert call[1]['x'] == expected_dates[i]

    @mock.patch('milestones.plt')
    def test_labels_match_exactly(self, mock_plt):
        axes = mock.Mock()
        milestones = {
            '2017-06-01': 'Transformer',
            '2022-11-01': 'ChatGPT'
        }
        overlay_milestones(axes, milestones)
        calls = axes.text.call_args_list  # Assuming text is used for labels
        expected_labels = ['Transformer', 'ChatGPT']
        for i, call in enumerate(calls):
            assert call[0][2] == expected_labels[i]  # Third arg is text

    @mock.patch('milestones.plt')
    def test_markers_in_correct_order(self, mock_plt):
        axes = mock.Mock()
        milestones = {
            '2023-08-01': 'Cursor and AI IDEs',
            '2022-11-01': 'ChatGPT',
            '2017-06-01': 'Transformer'
        }
        overlay_milestones(axes, milestones)
        calls = axes.axvline.call_args_list
        # Should be in date order: 2017, 2022, 2023
        expected_order = [pd.to_datetime('2017-06-01'), pd.to_datetime('2022-11-01'), pd.to_datetime('2023-08-01')]
        for i, call in enumerate(calls):
            assert call[1]['x'] == expected_order[i]