import pytest
from src.currency_logger import log_currency

def test_default_currency_logging():
    """Test default USD logging with 2 decimal places"""
    assert log_currency(1234.56) == '$1,234.56'

def test_custom_currency_symbol():
    """Test logging with a custom currency symbol"""
    assert log_currency(1234.56, currency='â¬') == 'â¬1,234.56'

def test_different_decimal_places():
    """Test logging with different decimal place precision"""
    assert log_currency(1234.56, decimal_places=3) == '$1,234.560'
    assert log_currency(1234.56, decimal_places=0) == '$1,235'

def test_integer_input():
    """Test logging with integer input"""
    assert log_currency(1234) == '$1,234.00'

def test_zero_input():
    """Test logging zero value"""
    assert log_currency(0) == '$0.00'

def test_negative_input():
    """Test logging negative numbers"""
    assert log_currency(-1234.56) == '$-1,234.56'

def test_invalid_type_raises_error():
    """Test that non-numeric input raises TypeError"""
    with pytest.raises(TypeError):
        log_currency('not a number')

def test_negative_decimal_places_raises_error():
    """Test that negative decimal places raise ValueError"""
    with pytest.raises(ValueError):
        log_currency(1234, decimal_places=-1)