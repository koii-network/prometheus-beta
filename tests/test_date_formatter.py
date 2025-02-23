import pytest
from datetime import date
from src.date_formatter import get_current_date_formatted

def test_get_current_date_formatted():
    """
    Test that the function returns the current date in correct format.
    """
    # Get the current date
    today = date.today()
    
    # Call the function
    formatted_date = get_current_date_formatted()
    
    # Check the format matches YYYY-MM-DD
    assert len(formatted_date) == 10, "Date should be 10 characters long"
    assert formatted_date.count('-') == 2, "Date should contain two hyphens"
    
    # Check the date matches today's date
    assert formatted_date == today.strftime('%Y-%m-%d'), "Formatted date should match today's date"

def test_return_type():
    """
    Test that the function returns a string.
    """
    result = get_current_date_formatted()
    assert isinstance(result, str), "Function should return a string"