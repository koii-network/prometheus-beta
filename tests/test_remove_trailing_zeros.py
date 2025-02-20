import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros():
    # Test cases with trailing zeros
    assert remove_trailing_zeros(1000) == 1
    assert remove_trailing_zeros(10200) == 102
    assert remove_trailing_zeros(30000) == 3
    
    # Test edge cases
    assert remove_trailing_zeros(0) == 0
    assert remove_trailing_zeros(10) == 1
    assert remove_trailing_zeros(1) == 1
    
    # Test error cases
    with pytest.raises(ValueError):
        remove_trailing_zeros(-100)
    
    with pytest.raises(ValueError):
        remove_trailing_zeros(3.14)
    
    with pytest.raises(ValueError):
        remove_trailing_zeros("100")