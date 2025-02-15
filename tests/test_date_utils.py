import pytest
from datetime import date
from src.date_utils import get_current_date_formatted

def test_get_current_date_formatted():
    """
    Test that the function returns the current date in YYYY-MM-DD format
    """
    # Get the current date directly from date.today()
    expected_date = date.today().strftime('%Y-%m-%d')
    
    # Call the function
    result = get_current_date_formatted()
    
    # Assert the result matches the expected format and current date
    assert result == expected_date, f"Expected {expected_date}, but got {result}"
    
    # Additional format validation
    assert len(result) == 10, "Date string should be exactly 10 characters long"
    assert result[4] == '-', "Fifth character should be a hyphen"
    assert result[7] == '-', "Eighth character should be a hyphen"
    
    # Validate year, month, and day are valid
    year, month, day = result.split('-')
    assert len(year) == 4, "Year should be 4 digits"
    assert len(month) == 2, "Month should be 2 digits"
    assert len(day) == 2, "Day should be 2 digits"
    
    # Additional checks to ensure it's a valid date
    try:
        date.fromisoformat(result)
    except ValueError:
        pytest.fail("Result is not a valid ISO format date")