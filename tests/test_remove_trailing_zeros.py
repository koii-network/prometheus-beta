import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros():
    # Test various inputs with trailing zeros
    assert remove_trailing_zeros(1000) == 1
    assert remove_trailing_zeros(10200) == 102
    assert remove_trailing_zeros(50000) == 5
    
    # Test zero input
    assert remove_trailing_zeros(0) == 0
    
    # Test single digit numbers
    assert remove_trailing_zeros(5) == 5
    assert remove_trailing_zeros(10) == 1
    
    # Test large numbers
    assert remove_trailing_zeros(1000000) == 1
    assert remove_trailing_zeros(10050000) == 1005
    
    # Test error case
    with pytest.raises(ValueError):
        remove_trailing_zeros(-100)