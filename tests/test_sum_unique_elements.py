import pytest
from src.sum_unique_elements import sum_unique_elements

def test_sum_unique_elements_basic():
    # Test basic scenario with some duplicates
    assert sum_unique_elements([1, 2, 3, 2]) == 4  # 1 + 3
    assert sum_unique_elements([1, 1, 2, 2]) == 0  # No unique elements
    assert sum_unique_elements([1, 2, 3, 4]) == 10  # All elements unique

def test_sum_unique_elements_complex():
    # Test more complex scenarios
    assert sum_unique_elements([1, 2, 2, 3, 3, 4]) == 4  # Only 1 and 4 are unique
    assert sum_unique_elements([]) == 0  # Empty list
    assert sum_unique_elements([5, 5, 5, 5]) == 0  # All duplicates

def test_sum_unique_elements_mixed():
    # Test mixed scenarios
    assert sum_unique_elements([-1, 1, -1, 2]) == 2  # Handles negative numbers
    assert sum_unique_elements([0, 0, 1, 1]) == 0  # Zero and multiple duplicates

def test_sum_unique_elements_types():
    # Ensure it handles different types of integers
    with pytest.raises(TypeError):
        sum_unique_elements(['a', 'b', 'c'])  # Non-integer input