import pytest
from src.count_pairs_with_difference import count_pairs_with_difference_of_five

def test_basic_functionality():
    # Basic test cases
    assert count_pairs_with_difference_of_five([1, 6, 3, 8, 9, 4]) == 2
    assert count_pairs_with_difference_of_five([5, 10, 15, 20]) == 3
    assert count_pairs_with_difference_of_five([1, 2, 3, 4, 5]) == 0

def test_empty_list():
    # Test with an empty list
    assert count_pairs_with_difference_of_five([]) == 0

def test_single_element_list():
    # Test with a single element list
    assert count_pairs_with_difference_of_five([1]) == 0

def test_negative_numbers():
    # Test with negative numbers
    assert count_pairs_with_difference_of_five([-1, 4, -6, -1, 3]) == 2

def test_invalid_input_types():
    # Test with invalid input types
    with pytest.raises(TypeError):
        count_pairs_with_difference_of_five("not a list")
    
    with pytest.raises(TypeError):
        count_pairs_with_difference_of_five(None)

def test_non_integer_elements():
    # Test with non-integer elements
    with pytest.raises(ValueError):
        count_pairs_with_difference_of_five([1, 2, "3", 4])
    
    with pytest.raises(ValueError):
        count_pairs_with_difference_of_five([1.5, 6.5, 2, 7])