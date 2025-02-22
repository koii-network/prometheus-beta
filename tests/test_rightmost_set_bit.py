import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_find_rightmost_set_bit():
    # Test basic cases
    assert find_rightmost_set_bit(0) == 0      # No set bits
    assert find_rightmost_set_bit(1) == 1      # First bit set
    assert find_rightmost_set_bit(8) == 4      # Fourth bit set
    assert find_rightmost_set_bit(16) == 5     # Fifth bit set
    
    # Test multiple set bits
    assert find_rightmost_set_bit(10) == 2     # Binary 1010 - rightmost set bit at 2nd position
    assert find_rightmost_set_bit(7) == 1      # Binary 111 - rightmost at 1st position
    
    # Large number test
    assert find_rightmost_set_bit(1024) == 11  # 2^10, 11th bit set
    
    # Error handling
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not a number")
    
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    
    with pytest.raises(ValueError):
        find_rightmost_set_bit(-5)