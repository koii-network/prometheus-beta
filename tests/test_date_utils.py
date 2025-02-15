from datetime import date
import pytest
from src.date_utils import get_current_date

def test_get_current_date():
    """Test that get_current_date returns the correct format."""
    current_date = get_current_date()
    
    # Check that the result is a string
    assert isinstance(current_date, str)
    
    # Check the format matches YYYY-MM-DD
    assert len(current_date) == 10
    assert current_date[4] == '-'
    assert current_date[7] == '-'
    
    # Check that the date matches today's date
    today = date.today().strftime("%Y-%m-%d")
    assert current_date == today