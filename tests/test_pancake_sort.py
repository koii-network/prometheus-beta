import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pancake_sort import pancake_sort

def test_pancake_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_already_sorted():
    """Test a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert pancake_sort(input_list) == input_list

def test_pancake_sort_reverse_sorted():
    """Test a list sorted in descending order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_with_duplicates():
    """Test a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_empty_list():
    """Test an empty list"""
    input_list = []
    assert pancake_sort(input_list) == []

def test_pancake_sort_single_element():
    """Test a list with a single element"""
    input_list = [42]
    assert pancake_sort(input_list) == [42]

def test_pancake_sort_float_list():
    """Test sorting a list of floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert pancake_sort(input_list) == expected

def test_pancake_sort_invalid_input():
    """Test that a TypeError is raised for invalid input"""
    with pytest.raises(TypeError):
        pancake_sort("not a list")
    with pytest.raises(TypeError):
        pancake_sort(None)

def test_pancake_sort_non_comparable():
    """Test handling of non-comparable elements"""
    class NonComparable:
        pass
    
    with pytest.raises(TypeError):
        pancake_sort([NonComparable(), NonComparable()])