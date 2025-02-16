import pytest
from src.gcd import greatest_common_divisor

def test_gcd_positive_numbers():
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(17, 23) == 1

def test_gcd_one_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

def test_gcd_both_zero():
    assert greatest_common_divisor(0, 0) == 0

def test_gcd_equal_numbers():
    assert greatest_common_divisor(7, 7) == 7

def test_gcd_invalid_inputs():
    with pytest.raises(TypeError):
        greatest_common_divisor(10.5, 5)
    
    with pytest.raises(TypeError):
        greatest_common_divisor("10", 5)
    
    with pytest.raises(ValueError):
        greatest_common_divisor(-10, 5)
    
    with pytest.raises(ValueError):
        greatest_common_divisor(10, -5)