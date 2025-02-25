import pytest
from src.patience_sort import patience_sort

def test_basic_integer_sort():
    """Test sorting a list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(input_list) == sorted(input_list)

def test_empty_list():
    """Test sorting an empty list"""
    assert patience_sort([]) == []

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert patience_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert patience_sort(input_list) == sorted(input_list)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 4, 4, 2, 2]
    assert patience_sort(input_list) == sorted(input_list)

def test_custom_key_sorting():
    """Test sorting with a custom key function"""
    input_list = [('apple', 5), ('banana', 3), ('cherry', 7)]
    
    # Sort by second element (weight)
    result = patience_sort(input_list, key=lambda x: x[1])
    assert result == [('banana', 3), ('apple', 5), ('cherry', 7)]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        patience_sort("not a list")

def test_mixed_type_sorting():
    """Test sorting a list with mixed types using a key function"""
    input_list = [5, 'a', 3, 'b', 1, 'c']
    
    # Sort by string representation
    result = patience_sort(input_list, key=str)
    assert result == [1, 3, 5, 'a', 'b', 'c']

def test_large_list_performance():
    """Test sorting a larger list to ensure performance"""
    import random
    input_list = random.sample(range(1000), 500)
    assert patience_sort(input_list) == sorted(input_list)