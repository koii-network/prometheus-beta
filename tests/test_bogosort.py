import pytest
import random
from src.bogosort import bogosort

def test_bogosort_empty_list():
    """Test sorting an empty list."""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a list with a single element."""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test sorting a list that is already sorted."""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_reversed_list():
    """Test sorting a reversed list."""
    reversed_list = [5, 4, 3, 2, 1]
    assert bogosort(reversed_list) == [1, 2, 3, 4, 5]

def test_bogosort_random_list():
    """Test sorting a random list of integers."""
    # Set a random seed for reproducibility
    random.seed(42)
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bogosort(input_list) == sorted(input_list)

def test_bogosort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bogosort(input_list) == sorted(input_list)

def test_bogosort_strings():
    """Test sorting a list of strings."""
    input_list = ['banana', 'apple', 'cherry', 'date']
    assert bogosort(input_list) == sorted(input_list)

def test_bogosort_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        bogosort(None)
    
    with pytest.raises(TypeError):
        bogosort("not a list")
    
    with pytest.raises(TypeError):
        bogosort(123)

def test_bogosort_preserves_original_list():
    """Ensure the original list is not modified."""
    original_list = [3, 1, 4, 1, 5]
    bogosort(original_list)
    assert original_list == [3, 1, 4, 1, 5]