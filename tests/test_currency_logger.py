import pytest
from src.currency_logger import format_currency_number

def test_default_currency_format():
    assert format_currency_number(100) == '$100.00'
    assert format_currency_number(100.50) == '$100.50'

def test_custom_currency_symbol():
    assert format_currency_number(100, currency='â¬') == 'â¬100.00'
    assert format_currency_number(100.50, currency='Â£') == 'Â£100.50'

def test_custom_decimal_places():
    assert format_currency_number(100, decimal_places=0) == '$100'
    assert format_currency_number(100.5678, decimal_places=3) == '$100.568'

def test_integer_input():
    assert format_currency_number(100) == '$100.00'
    assert format_currency_number(0) == '$0.00'

def test_float_input():
    assert format_currency_number(100.25) == '$100.25'
    assert format_currency_number(0.50) == '$0.50'

def test_negative_number():
    assert format_currency_number(-100) == '$-100.00'
    assert format_currency_number(-100.50) == '$-100.50'

def test_invalid_input_types():
    with pytest.raises(TypeError):
        format_currency_number('100')
    
    with pytest.raises(TypeError):
        format_currency_number(None)

def test_invalid_decimal_places():
    with pytest.raises(ValueError):
        format_currency_number(100, decimal_places=-1)