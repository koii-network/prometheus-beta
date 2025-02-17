import pytest
from datetime import date
from src.date_utils import get_current_date

def test_get_current_date():
    """
    Test that get_current_date returns the current date in YYYY-MM-DD format
    """
    # Get the current date using datetime
    expected_date = date.today().strftime("%Y-%m-%d")
    
    # Call the function
    result = get_current_date()
    
    # Assert the result matches the expected format and value
    assert result == expected_date, f"Expected {expected_date}, but got {result}"
    
    # Check the format is exactly YYYY-MM-DD
    assert len(result) == 10, "Date string should be 10 characters long"
    assert result[4] == '-', "Fifth character should be a hyphen"
    assert result[7] == '-', "Eighth character should be a hyphen"
    
    # Check that each part is the correct length
    year, month, day = result.split('-')
    assert len(year) == 4, "Year should be 4 digits"
    assert len(month) == 2, "Month should be 2 digits"
    assert len(day) == 2, "Day should be 2 digits"