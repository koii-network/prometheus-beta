import pytest
from src.currency_logger import log_currency

def test_default_currency_logging():
    """Test default currency logging with USD symbol"""
    assert log_currency(1234.56) == '$1,234.56'

def test_different_currency_symbol():
    """Test logging with different currency symbols"""
    assert log_currency(1234.56, currency_symbol='€') == '€1,234.56'
    assert log_currency(1234.56, currency_symbol='£') == '£1,234.56'

def test_different_decimal_places():
    """Test logging with different decimal place counts"""
    assert log_currency(1234.56, decimal_places=0) == '$1,235'
    assert log_currency(1234.56, decimal_places=3) == '$1,234.560'

def test_integer_input():
    """Test logging with integer input"""
    assert log_currency(1234) == '$1,234.00'

def test_large_number():
    """Test logging with large numbers"""
    assert log_currency(1234567.89) == '$1,234,567.89'

def test_negative_input():
    """Test logging with negative numbers"""
    assert log_currency(-1234.56) == '$-1,234.56'

def test_invalid_input_type():
    """Test that TypeError is raised for non-numeric inputs"""
    with pytest.raises(TypeError):
        log_currency('not a number')

def test_negative_decimal_places():
    """Test that ValueError is raised for negative decimal places"""
    with pytest.raises(ValueError):
        log_currency(1234.56, decimal_places=-1)