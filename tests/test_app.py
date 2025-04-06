import pytest

from src.app import get_request
from unittest.mock import patch
from requests.exceptions import Timeout, RequestException


# Test API request and that output is json
def test_get_request():
    # Arrange
    with patch('requests.get') as mock_get:
        mock_data = {"symbol": "NVDA"}
        mock_get.return_value.json.return_value = mock_data
        # Act
        response = get_request('https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=NVDA&apikey=demo')
        # Assert
        assert response == mock_data


# Defining exceptions
@pytest.mark.parametrize("exception, error_message", [
    (
        Exception("An error occurred"),
        "An error occurred - Unexpected error for URL"
    ),
    (
        Timeout("The request timed out"),
        "The request timed out - Request failed for URL"
    ),
    (
        RequestException("Invalid URL"),
        "Invalid URL - Request failed for URL"
    )
])
# Testing exceptions
def test_get_request_handles_exceptions(exception, error_message):
    # Arrange
    with patch('requests.get') as mock_get:
        mock_get.side_effect = exception
        # Act
        with pytest.raises(RequestException) as exc_info:
            get_request('https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=NVDA&apikey=demo')
        # Assert
        assert str(exc_info.value) == error_message
