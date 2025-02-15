from datetime import date
import pytest
from src.date_utils import get_current_date

def test_get_current_date():
    """Test that get_current_date returns the current date in correct format."""
    current_date = get_current_date()
    
    # Check that the returned string matches the expected format
    assert len(current_date) == 10, "Date string should be 10 characters long"
    assert current_date.count('-') == 2, "Date string should contain two hyphens"
    
    # Verify the format matches YYYY-MM-DD
    try:
        # Try to parse the date to ensure it's a valid date
        parsed_date = date.fromisoformat(current_date)
        assert parsed_date == date.today(), "Returned date should be today's date"
    except ValueError:
        pytest.fail("Date is not in valid YYYY-MM-DD format")

def test_get_current_date_type():
    """Test that the function returns a string."""
    assert isinstance(get_current_date(), str), "Function should return a string"