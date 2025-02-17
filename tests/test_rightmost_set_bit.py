import pytest
from src.rightmost_set_bit import find_rightmost_set_bit_position

def test_rightmost_set_bit_basic_cases():
    # Verify basic cases of finding the rightmost set bit position
    assert find_rightmost_set_bit_position(0) == 0
    assert find_rightmost_set_bit_position(1) == 1
    assert find_rightmost_set_bit_position(2) == 2
    assert find_rightmost_set_bit_position(3) == 1
    assert find_rightmost_set_bit_position(8) == 4
    assert find_rightmost_set_bit_position(16) == 5

def test_rightmost_set_bit_larger_numbers():
    # Test larger numbers
    assert find_rightmost_set_bit_position(42) == 2  # 101010 in binary
    assert find_rightmost_set_bit_position(64) == 7
    assert find_rightmost_set_bit_position(100) == 3

def test_rightmost_set_bit_error_handling():
    # Test type and value error cases
    with pytest.raises(TypeError):
        find_rightmost_set_bit_position("not an int")
    
    with pytest.raises(TypeError):
        find_rightmost_set_bit_position(3.14)
    
    with pytest.raises(ValueError):
        find_rightmost_set_bit_position(-5)