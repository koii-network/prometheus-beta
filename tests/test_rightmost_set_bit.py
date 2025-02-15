import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_find_rightmost_set_bit():
    # Test basic cases
    assert find_rightmost_set_bit(0) == 0
    assert find_rightmost_set_bit(1) == 1
    assert find_rightmost_set_bit(2) == 2
    assert find_rightmost_set_bit(3) == 1
    assert find_rightmost_set_bit(8) == 4
    assert find_rightmost_set_bit(16) == 5

def test_find_rightmost_set_bit_larger_numbers():
    assert find_rightmost_set_bit(18) == 2  # 10010 in binary
    assert find_rightmost_set_bit(32) == 6
    assert find_rightmost_set_bit(100) == 3  # 1100100 in binary

def test_find_rightmost_set_bit_error_handling():
    # Test type errors
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not an int")
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)

    # Test negative number
    with pytest.raises(ValueError):
        find_rightmost_set_bit(-1)