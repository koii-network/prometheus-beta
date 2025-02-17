from datetime import date
import re
from src.date_utils import get_current_date_formatted

def test_get_current_date_formatted():
    """Test that the function returns a date in the correct format."""
    # Get the current date
    current_date = get_current_date_formatted()
    
    # Check that it's a string
    assert isinstance(current_date, str), "Return value should be a string"
    
    # Check format using regex (YYYY-MM-DD)
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', current_date), "Date should be in YYYY-MM-DD format"
    
    # Check that the date matches today's date
    assert current_date == date.today().strftime("%Y-%m-%d"), "Date should match current date"