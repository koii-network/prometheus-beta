import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros():
    # Test removing trailing zeros from various numbers
    assert remove_trailing_zeros(100) == 1
    assert remove_trailing_zeros(1000) == 1
    assert remove_trailing_zeros(10203000) == 10203
    assert remove_trailing_zeros(5000) == 5
    assert remove_trailing_zeros(0) == 0
    assert remove_trailing_zeros(42) == 42

def test_negative_input():
    # Test handling of negative inputs
    with pytest.raises(ValueError):
        remove_trailing_zeros(-100)

def test_non_integer_input():
    # Test handling of non-integer inputs
    with pytest.raises(ValueError):
        remove_trailing_zeros(100.5)
    with pytest.raises(ValueError):
        remove_trailing_zeros("1000")
    with pytest.raises(ValueError):
        remove_trailing_zeros(None)