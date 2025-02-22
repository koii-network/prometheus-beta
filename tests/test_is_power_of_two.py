import pytest
from src.is_power_of_two import is_power_of_two

def test_powers_of_two():
    """Test various powers of two"""
    assert is_power_of_two(1) == True   # 2^0
    assert is_power_of_two(2) == True   # 2^1
    assert is_power_of_two(4) == True   # 2^2
    assert is_power_of_two(8) == True   # 2^3
    assert is_power_of_two(16) == True  # 2^4
    assert is_power_of_two(32) == True  # 2^5

def test_non_powers_of_two():
    """Test numbers that are not powers of two"""
    assert is_power_of_two(0) == False
    assert is_power_of_two(3) == False
    assert is_power_of_two(5) == False
    assert is_power_of_two(6) == False
    assert is_power_of_two(7) == False
    assert is_power_of_two(15) == False

def test_large_powers_of_two():
    """Test larger powers of two"""
    assert is_power_of_two(1024) == True   # 2^10
    assert is_power_of_two(65536) == True  # 2^16

def test_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError):
        is_power_of_two(-1)
    with pytest.raises(ValueError):
        is_power_of_two(-16)