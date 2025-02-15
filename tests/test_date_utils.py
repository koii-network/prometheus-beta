import pytest
from datetime import date
from src.date_utils import get_current_date

def test_get_current_date_format():
    """Test that the date is returned in the correct YYYY-MM-DD format."""
    current_date = get_current_date()
    
    # Check that the date is a string
    assert isinstance(current_date, str)
    
    # Check the format is exactly YYYY-MM-DD (10 characters)
    assert len(current_date) == 10
    
    # Verify the format matches YYYY-MM-DD
    assert current_date.count('-') == 2
    assert current_date[4] == '-'
    assert current_date[7] == '-'

def test_get_current_date_matches_today():
    """Verify the returned date matches the current system date."""
    current_date = get_current_date()
    today = date.today().strftime("%Y-%m-%d")
    
    assert current_date == today