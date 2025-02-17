import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    """Test a standard increasing subsequence"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60]

def test_already_sorted():
    """Test when array is already sorted"""
    arr = [1, 2, 3, 4, 5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test when array is reverse sorted"""
    arr = [5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5]

def test_empty_list():
    """Test empty list"""
    arr = []
    result = find_longest_increasing_subsequence(arr)
    assert result == []

def test_single_element():
    """Test with a single element"""
    arr = [42]
    result = find_longest_increasing_subsequence(arr)
    assert result == [42]

def test_duplicate_elements():
    """Test with duplicate elements"""
    arr = [1, 2, 2, 3, 1, 4]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 2, 3, 4]

def test_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_non_comparable_elements():
    """Test with non-comparable elements"""
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, None, 4])

def test_mixed_types():
    """Test with mixed numeric types"""
    arr = [1, 2, 3.14, 4, 5.5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 2, 3.14, 4, 5.5]