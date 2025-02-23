import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_sequence():
    """Test a typical sequence with multiple increasing subsequences"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 6
    assert subsequence == [10, 22, 33, 50, 60, 80]

def test_already_sorted():
    """Test a fully sorted sequence"""
    arr = [1, 2, 3, 4, 5]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test a reverse sorted sequence"""
    arr = [5, 4, 3, 2, 1]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert len(subsequence) == 1
    assert subsequence[0] in arr

def test_empty_list():
    """Test an empty list"""
    arr = []
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 0
    assert subsequence == []

def test_single_element():
    """Test a list with a single element"""
    arr = [42]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert subsequence == [42]

def test_duplicate_elements():
    """Test a list with duplicate elements"""
    arr = [1, 2, 2, 3, 3, 4, 5]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [1, 2, 3, 4, 5]

def test_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_invalid_element_type():
    """Test handling of non-integer elements"""
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, "3", 4])

def test_complex_sequence():
    """Test a more complex sequence with non-linear increase"""
    arr = [7, 7, 7, 7, 7, 7, 7]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert len(subsequence) == 1
    assert subsequence[0] == 7