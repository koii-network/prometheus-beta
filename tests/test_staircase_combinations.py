import pytest
from src.staircase_combinations import count_staircase_combinations

def test_basic_cases():
    """Test basic staircase climbing scenarios."""
    assert count_staircase_combinations([1]) == [1]
    assert count_staircase_combinations([2]) == [2]
    assert count_staircase_combinations([3]) == [3]
    assert count_staircase_combinations([4]) == [5]

def test_multiple_staircases():
    """Test calculating combinations for multiple staircase lengths."""
    assert count_staircase_combinations([1, 2, 3, 4]) == [1, 2, 3, 5]

def test_large_staircases():
    """Test larger staircase lengths."""
    assert count_staircase_combinations([10]) == [89]
    assert count_staircase_combinations([15]) == [987]

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test zero and negative lengths
    assert count_staircase_combinations([0]) == [0]
    
    # Empty list
    assert count_staircase_combinations([]) == []

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Non-list input
    with pytest.raises(ValueError, match="Input must be a list of integers"):
        count_staircase_combinations(10)
    
    # List with non-integer values
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_staircase_combinations([1, 2, 'a'])
    
    # List with non-positive integers
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_staircase_combinations([1, 2, -3])
    
    # List with non-integer types
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_staircase_combinations([1, 2, 3.5])