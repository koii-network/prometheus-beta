import pytest
from src.count_occurrences import count_element_occurrences

def test_count_occurrences_basic():
    # Test basic functionality
    test_array = [1, 2, 3, 2, 2, 4, 5]
    assert count_element_occurrences(test_array, 2) == 3
    assert count_element_occurrences(test_array, 1) == 1
    assert count_element_occurrences(test_array, 6) == 0

def test_count_occurrences_empty_list():
    # Test with an empty list
    assert count_element_occurrences([], 1) == 0

def test_count_occurrences_different_types():
    # Test with different types of elements
    test_array = ['apple', 'banana', 'apple', 'cherry', 'apple']
    assert count_element_occurrences(test_array, 'apple') == 3
    assert count_element_occurrences(test_array, 'banana') == 1
    assert count_element_occurrences(test_array, 'grape') == 0

def test_count_occurrences_invalid_input():
    # Test with invalid input type
    with pytest.raises(TypeError):
        count_element_occurrences("not a list", 1)
    with pytest.raises(TypeError):
        count_element_occurrences(123, 1)
    with pytest.raises(TypeError):
        count_element_occurrences(None, 1)