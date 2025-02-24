import pytest
from src.currency_logger import format_currency_log

def test_default_usd_formatting():
    """Test default USD formatting"""
    assert format_currency_log(1234.56) == '$1234.56'

def test_different_currencies():
    """Test different currency symbols"""
    assert format_currency_log(1234.56, currency='EUR') == '€1234.56'
    assert format_currency_log(1234.56, currency='GBP') == '£1234.56'
    assert format_currency_log(1234.56, currency='JPY') == '¥1234.56'

def test_custom_precision():
    """Test custom decimal precision"""
    assert format_currency_log(1234.5678, precision=3) == '$1234.568'
    assert format_currency_log(1234, precision=0) == '$1234'

def test_zero_amount():
    """Test zero amount formatting"""
    assert format_currency_log(0) == '$0.00'

def test_integer_input():
    """Test integer input"""
    assert format_currency_log(1234) == '$1234.00'

def test_negative_amount_error():
    """Test that negative amounts raise a ValueError"""
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        format_currency_log(-100)

def test_invalid_type_error():
    """Test that non-numeric inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Amount must be a number"):
        format_currency_log("not a number")

def test_invalid_precision_error():
    """Test that negative precision raises a ValueError"""
    with pytest.raises(ValueError, match="Precision cannot be negative"):
        format_currency_log(100, precision=-1)

def test_unknown_currency():
    """Test unknown currency defaults to no symbol"""
    assert format_currency_log(1234.56, currency='CAD') == '1234.56'