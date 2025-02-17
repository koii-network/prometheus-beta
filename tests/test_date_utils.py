import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date string in different formats"""
    # Test with yyyy-mm-dd format
    result = add_days_to_date('2023-05-15', 5)
    assert result == datetime(2023, 5, 20)
    
    # Test with mm/dd/yyyy format
    result = add_days_to_date('05/15/2023', 10)
    assert result == datetime(2023, 5, 25)

def test_add_days_to_date_datetime_input():
    """Test adding days to a datetime object"""
    input_date = datetime(2023, 5, 15)
    result = add_days_to_date(input_date, 7)
    assert result == datetime(2023, 5, 22)

def test_add_zero_days():
    """Test adding zero days"""
    result = add_days_to_date('2023-05-15', 0)
    assert result == datetime(2023, 5, 15)

def test_add_negative_days():
    """Test adding negative days"""
    result = add_days_to_date('2023-05-15', -5)
    assert result == datetime(2023, 5, 10)

def test_invalid_date_type():
    """Test raising TypeError for invalid input types"""
    with pytest.raises(TypeError, match="input_date must be a string or datetime object"):
        add_days_to_date(123, 5)

def test_invalid_days_type():
    """Test raising TypeError for invalid days type"""
    with pytest.raises(TypeError, match="days_to_add must be an integer"):
        add_days_to_date('2023-05-15', '5')

def test_invalid_date_string():
    """Test raising ValueError for invalid date string"""
    with pytest.raises(ValueError, match="Unable to parse date"):
        add_days_to_date('invalid-date', 5)