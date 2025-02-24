import pytest
from src.second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 4, 3, 2, 1]) == 4
    assert find_second_largest([10, 5, 8, 12, 3]) == 10

def test_find_second_largest_with_duplicates():
    """Test finding second largest when there are duplicate numbers."""
    assert find_second_largest([5, 5, 4, 3, 2]) == 4
    assert find_second_largest([5, 5, 4, 4, 3]) == 4

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([0, -5, 10, -3, 7]) == 7

def test_find_second_largest_error_cases():
    """Test error cases for second largest."""
    # Empty array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])
    
    # Single element array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])
    
    # Array with all same elements
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([5, 5, 5, 5])

def test_find_second_largest_single_duplicate():
    """Test case with a single duplicate."""
    assert find_second_largest([3, 3, 1, 2]) == 2