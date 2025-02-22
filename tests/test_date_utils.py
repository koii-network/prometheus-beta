from datetime import date
import pytest
from src.date_utils import get_current_date

def test_get_current_date_format():
    """
    Test that the get_current_date function returns 
    a string in the correct YYYY-MM-DD format.
    """
    current_date = get_current_date()
    
    # Check that the date string is exactly 10 characters long
    assert len(current_date) == 10
    
    # Check format pattern: YYYY-MM-DD
    assert current_date[4] == '-'
    assert current_date[7] == '-'
    
    # Validate that it matches today's date
    assert current_date == date.today().strftime("%Y-%m-%d")

def test_get_current_date_return_type():
    """
    Test that the function returns a string.
    """
    assert isinstance(get_current_date(), str)