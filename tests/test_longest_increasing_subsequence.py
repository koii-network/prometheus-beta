import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    """Test a standard increasing subsequence scenario"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [10, 22, 33, 50, 60]

def test_already_sorted():
    """Test an already sorted array"""
    arr = [1, 2, 3, 4, 5]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test a reverse sorted array"""
    arr = [5, 4, 3, 2, 1]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert len(subsequence) == 1

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

def test_with_duplicates():
    """Test an array with duplicate elements"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 6
    assert subsequence == [0, 2, 6, 9, 13, 15]

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_invalid_element_type():
    """Test that a list with non-numeric elements raises a ValueError"""
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, "three", 4])