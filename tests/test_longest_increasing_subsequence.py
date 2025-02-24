import pytest
from src.longest_increasing_subsequence import find_lis_length

def test_basic_sequences():
    """Test various basic increasing subsequence scenarios."""
    assert find_lis_length([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert find_lis_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_edge_cases():
    """Test edge cases like empty list, single element, and non-increasing list."""
    assert find_lis_length([]) == 0
    assert find_lis_length([5]) == 1
    assert find_lis_length([5, 4, 3, 2, 1]) == 1
    assert find_lis_length([1, 1, 1, 1]) == 1

def test_already_sorted():
    """Test list that is already sorted."""
    assert find_lis_length([1, 2, 3, 4, 5]) == 5

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_lis_length(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        find_lis_length(None)
    
    with pytest.raises(ValueError, match="All elements must be integers"):
        find_lis_length([1, 2, 'a', 4])
    
    with pytest.raises(ValueError, match="All elements must be integers"):
        find_lis_length([1, 2, 3.14, 4])

def test_negative_numbers():
    """Test sequences with negative numbers."""
    assert find_lis_length([-7, -6, -5, -4]) == 4
    assert find_lis_length([-5, 2, -1, 3, 4]) == 3

def test_mixed_order():
    """Test sequences with mixed order and multiple possible subsequences."""
    assert find_lis_length([3, 1, 4, 1, 5, 9, 2, 6, 5]) == 4