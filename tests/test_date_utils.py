import pytest
from datetime import date
from src.date_utils import get_current_date

def test_get_current_date():
    """Test that get_current_date returns the correct format."""
    current_date = get_current_date()
    
    # Check format: YYYY-MM-DD
    assert len(current_date) == 10, "Date should be 10 characters long"
    assert current_date[4] == '-', "Year and month should be separated by '-'"
    assert current_date[7] == '-', "Month and day should be separated by '-'"
    
    # Verify it matches the current date
    today = date.today().strftime('%Y-%m-%d')
    assert current_date == today, "Returned date should match today's date"

def test_get_current_date_type():
    """Test that the function returns a string."""
    assert isinstance(get_current_date(), str), "Function should return a string"