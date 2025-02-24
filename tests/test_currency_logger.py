import pytest
from src.currency_logger import log_currency

def test_default_currency_formatting():
    assert log_currency(1234.56) == '$1,234.56'

def test_custom_currency_symbol():
    assert log_currency(1234.56, currency='â¬') == 'â¬1,234.56'

def test_different_decimal_places():
    assert log_currency(1234.56, decimal_places=0) == '$1,235'
    assert log_currency(1234.56, decimal_places=3) == '$1,234.560'

def test_integer_input():
    assert log_currency(1234) == '$1,234.00'

def test_large_number():
    assert log_currency(1234567.89) == '$1,234,567.89'

def test_negative_number():
    assert log_currency(-1234.56) == '$-1,234.56'

def test_zero():
    assert log_currency(0) == '$0.00'

def test_type_error():
    with pytest.raises(TypeError):
        log_currency('not a number')

def test_negative_decimal_places():
    with pytest.raises(ValueError):
        log_currency(1234.56, decimal_places=-1)