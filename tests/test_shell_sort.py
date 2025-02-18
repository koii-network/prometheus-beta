import pytest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.shell_sort import shell_sort

def test_shell_sort_normal_list():
    """Test shell sort with a normal list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert shell_sort(arr) == sorted(arr)

def test_shell_sort_already_sorted():
    """Test shell sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert shell_sort(arr) == sorted(arr)

def test_shell_sort_reverse_sorted():
    """Test shell sort with a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert shell_sort(arr) == sorted(arr)

def test_shell_sort_empty_list():
    """Test shell sort with an empty list"""
    arr = []
    assert shell_sort(arr) == []

def test_shell_sort_single_element():
    """Test shell sort with a single element"""
    arr = [42]
    assert shell_sort(arr) == [42]

def test_shell_sort_duplicate_elements():
    """Test shell sort with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert shell_sort(arr) == sorted(arr)

def test_shell_sort_large_list():
    """Test shell sort with a larger list"""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] * 10
    assert shell_sort(arr) == sorted(arr)

def test_shell_sort_negative_numbers():
    """Test shell sort with negative numbers"""
    arr = [-4, 1, -9, 0, 5, -2]
    assert shell_sort(arr) == sorted(arr)

def test_shell_sort_invalid_input_type():
    """Test shell sort with invalid input type"""
    with pytest.raises(TypeError):
        shell_sort("not a list")

def test_shell_sort_original_list_unchanged():
    """Verify that the original list remains unchanged"""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    shell_sort(arr)
    assert arr == original