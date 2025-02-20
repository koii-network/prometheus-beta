import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros():
    # Test cases with trailing zeros
    assert remove_trailing_zeros(1000) == 1
    assert remove_trailing_zeros(10200) == 102
    assert remove_trailing_zeros(50000) == 5
    
    # Test special case for 0
    assert remove_trailing_zeros(0) == 0
    
    # Test single digit numbers
    assert remove_trailing_zeros(5) == 5
    assert remove_trailing_zeros(10) == 1
    
    # Edge cases
    assert remove_trailing_zeros(100000000) == 1
    
    # Error cases
    with pytest.raises(ValueError):
        remove_trailing_zeros(-100)
    
    with pytest.raises(ValueError):
        remove_trailing_zeros(3.14)
    
    with pytest.raises(ValueError):
        remove_trailing_zeros("1000")