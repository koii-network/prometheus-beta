import pytest
from datetime import date
from src.date_utils import get_current_date

def test_get_current_date():
    """
    Test the get_current_date function returns correct format and current date
    """
    # Get the current date 
    current_date = date.today()
    
    # Call the function
    result = get_current_date()
    
    # Assert the result matches expected format
    assert isinstance(result, str), "Result should be a string"
    assert len(result) == 10, "Date string should be 10 characters long (YYYY-MM-DD)"
    
    # Check format components
    assert result.count('-') == 2, "Date should contain two hyphens"
    
    # Verify the date matches today's date
    assert result == current_date.strftime("%Y-%m-%d"), "Date should match current date"

def test_get_current_date_format():
    """
    Test the specific format of the date string
    """
    result = get_current_date()
    
    # Split the date into parts
    parts = result.split('-')
    
    # Check year part
    assert len(parts[0]) == 4, "Year should be 4 digits"
    assert parts[0].isdigit(), "Year should be numeric"
    
    # Check month part
    assert len(parts[1]) == 2, "Month should be 2 digits"
    assert parts[1].isdigit(), "Month should be numeric"
    assert 1 <= int(parts[1]) <= 12, "Month should be between 01 and 12"
    
    # Check day part
    assert len(parts[2]) == 2, "Day should be 2 digits"
    assert parts[2].isdigit(), "Day should be numeric"
    assert 1 <= int(parts[2]) <= 31, "Day should be between 01 and 31"