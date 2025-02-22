import pytest
from src.gcd_recursive import gcd_recursive

def test_gcd_basic_cases():
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5

def test_gcd_same_number():
    assert gcd_recursive(7, 7) == 7
    assert gcd_recursive(0, 0) == 0

def test_gcd_negative_input():
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd_recursive(-10, 20)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd_recursive(10, -20)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        gcd_recursive(-10, -20)