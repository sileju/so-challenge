"""

Tests for data_fetcher module.

"""

import pytest
import pandas as pd
from unittest import mock
import os
import requests
from data_fetcher import fetch_so_data


class TestDataFetcher:
    @mock.patch('data_fetcher.requests.get')
    def test_successful_data_fetch(self, mock_get):
        # Mock API response
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            'items': [
                {'creation_date': 1199145600},  # Jan 2008
                {'creation_date': 1201824000},  # Feb 2008
                # Add more for full month, but for test, assume it returns counts
            ],
            'has_more': False
        }
        mock_get.return_value = mock_response

        # Mock the processing to return a DataFrame
        # Assuming the function processes the data
        df = fetch_so_data()

        assert isinstance(df, pd.DataFrame)
        assert list(df.columns) == ['year_month', 'question_count']
        # For 17 years * 12 months = 204 rows
        assert df.shape[0] == 204

    @mock.patch('data_fetcher.requests.get')
    @mock.patch('data_fetcher.os.path.exists')
    @mock.patch('data_fetcher.pd.read_csv')
    def test_cached_data_returned(self, mock_read_csv, mock_exists, mock_get):
        mock_exists.return_value = True
        mock_df = pd.DataFrame({'year_month': ['2008-01'], 'question_count': [100]})
        mock_read_csv.return_value = mock_df

        df = fetch_so_data()

        # Should not call API
        mock_get.assert_not_called()
        pd.testing.assert_frame_equal(df, mock_df)

    @mock.patch('data_fetcher.requests.get')
    @mock.patch('data_fetcher.time.sleep')  # If sleep is used for retries
    @mock.patch('data_fetcher.os.path.exists')
    def test_network_error_retry(self, mock_exists, mock_sleep, mock_get):
        mock_exists.return_value = False  # No cache
        call_count = 0
        def side_effect(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count <= 2:
                raise requests.RequestException("Network error")
            mock_response = mock.Mock()
            mock_response.json.return_value = {'items': [], 'has_more': False}
            return mock_response
        mock_get.side_effect = side_effect

        df = fetch_so_data()

        # Should have called get at least 3 times for retries
        assert mock_get.call_count >= 3
        assert mock_sleep.call_count >= 2