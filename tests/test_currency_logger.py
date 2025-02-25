import pytest
import logging
from src.currency_logger import format_currency

def test_default_currency_formatting():
    # Test default $ symbol and basic formatting
    result = format_currency(1234.56)
    assert result == "$1,234.56"

def test_custom_currency_symbol():
    # Test custom currency symbol
    result = format_currency(1234.56, currency_symbol='â¬')
    assert result == "â¬1,234.56"

def test_whole_number_formatting():
    # Test whole number formatting
    result = format_currency(1000)
    assert result == "$1,000.00"

def test_zero_formatting():
    # Test zero formatting
    result = format_currency(0)
    assert result == "$0.00"

def test_invalid_input_type():
    # Test TypeError for non-numeric input
    with pytest.raises(TypeError, match="Input must be a numeric value"):
        format_currency("not a number")

def test_negative_number():
    # Test ValueError for negative number
    with pytest.raises(ValueError, match="Number must be non-negative"):
        format_currency(-100)

def test_logging(caplog):
    # Test logging functionality
    caplog.set_level(logging.INFO)
    format_currency(500.25)
    
    assert "Logged currency: $500.25" in caplog.text