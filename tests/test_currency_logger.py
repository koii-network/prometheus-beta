import pytest
import logging
import src.currency_logger as currency_logger

def test_log_currency_number_default():
    # Test default USD formatting
    result = currency_logger.log_currency_number(1234.56)
    assert result == "$1,234.56"

def test_log_currency_number_custom_symbol():
    # Test custom currency symbol
    result = currency_logger.log_currency_number(1234.56, currency='â¬')
    assert result == "â¬1,234.56"

def test_log_currency_number_integer():
    # Test integer input
    result = currency_logger.log_currency_number(1234)
    assert result == "$1,234.00"

def test_log_currency_number_invalid_type():
    # Test invalid type raises TypeError
    with pytest.raises(TypeError):
        currency_logger.log_currency_number("not a number")

def test_log_currency_number_invalid_currency():
    # Test invalid currency symbol raises ValueError
    with pytest.raises(ValueError):
        currency_logger.log_currency_number(1234, currency='')

def test_log_currency_number_large_number():
    # Test large number formatting
    result = currency_logger.log_currency_number(1234567.89)
    assert result == "$1,234,567.89"