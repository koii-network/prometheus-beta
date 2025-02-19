import pytest
from src.two_sum_check import two_sum_check

def test_two_sum_check_existing_pair():
    """Test finding a pair that sums to the target."""
    assert two_sum_check([1, 2, 3, 4, 5], 7) == True
    assert two_sum_check([10, 15, 3, 7], 17) == True

def test_two_sum_check_no_pair():
    """Test when no pair sums to the target."""
    assert two_sum_check([1, 2, 3, 4, 5], 20) == False
    assert two_sum_check([10, 15, 20, 25], 5) == False

def test_two_sum_check_edge_cases():
    """Test edge cases like minimum list size and exact target."""
    assert two_sum_check([5, 10], 15) == True
    assert two_sum_check([0, -1, 1], 0) == True

def test_two_sum_check_error_cases():
    """Test error cases like empty list or duplicate values."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        two_sum_check([], 10)
    
    with pytest.raises(ValueError, match="Input list must contain unique integers"):
        two_sum_check([1, 2, 2, 3], 4)