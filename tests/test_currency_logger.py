import pytest
from src.currency_logger import log_currency

def test_default_currency_formatting():
    """Test default USD formatting"""
    assert log_currency(1234.56) == "$1,234.56"

def test_custom_currency_symbol():
    """Test custom currency symbol"""
    assert log_currency(1234.56, currency='€') == "€1,234.56"

def test_different_decimal_places():
    """Test different decimal place formatting"""
    assert log_currency(1234.56, decimal_places=3) == "$1,234.560"

def test_integer_input():
    """Test integer input"""
    assert log_currency(1234) == "$1,234.00"

def test_zero_input():
    """Test zero input"""
    assert log_currency(0) == "$0.00"

def test_negative_number():
    """Test negative number formatting"""
    assert log_currency(-1234.56) == "$-1,234.56"

def test_invalid_number_type():
    """Test raising TypeError for non-numeric input"""
    with pytest.raises(TypeError):
        log_currency("not a number")

def test_negative_decimal_places():
    """Test raising ValueError for negative decimal places"""
    with pytest.raises(ValueError):
        log_currency(1234, decimal_places=-1)