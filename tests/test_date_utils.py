import pytest
from datetime import date
from src.date_utils import get_current_date

def test_get_current_date():
    """
    Test that get_current_date returns the current date in YYYY-MM-DD format.
    """
    # Get the current date and format it as expected
    expected_date = date.today().strftime("%Y-%m-%d")
    
    # Call the function
    result = get_current_date()
    
    # Assert the result matches the expected format and value
    assert result == expected_date, f"Expected {expected_date}, but got {result}"
    
def test_get_current_date_format():
    """
    Test the specific format of the returned date string.
    """
    result = get_current_date()
    
    # Check length (YYYY-MM-DD is always 10 characters)
    assert len(result) == 10, f"Date string should be 10 characters long, got {len(result)}"
    
    # Check format (YYYY-MM-DD)
    assert result[4] == '-', "Fifth character should be a hyphen"
    assert result[7] == '-', "Eighth character should be a hyphen"
    
    # Verify each part is numeric
    year, month, day = result.split('-')
    assert year.isdigit() and len(year) == 4, "Year should be 4 numeric digits"
    assert month.isdigit() and len(month) == 2, "Month should be 2 numeric digits"
    assert day.isdigit() and len(day) == 2, "Day should be 2 numeric digits"