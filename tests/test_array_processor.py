import pytest
from src.array_processor import process_multi_dimensional_array

def test_process_multi_dimensional_array_basic():
    input_array = [[1, 2], [3, 4], [5, 6]]
    expected = [6, 5, 4, 3, 2, 1]
    assert process_multi_dimensional_array(input_array) == expected

def test_process_multi_dimensional_array_with_empty_subarrays():
    input_array = [[1, 2], [], [3, 4], [], [5, 6]]
    expected = [6, 5, 4, 3, 2, 1]
    assert process_multi_dimensional_array(input_array) == expected

def test_process_multi_dimensional_array_with_duplicates():
    input_array = [[1, 2, 2], [3, 3, 4], [1, 5]]
    expected = [4, 3, 2, 1, 5]
    assert process_multi_dimensional_array(input_array) == expected

def test_process_multi_dimensional_array_empty_input():
    input_array = []
    expected = []
    assert process_multi_dimensional_array(input_array) == expected

def test_process_multi_dimensional_array_nested():
    input_array = [[1, [2, 3]], [4, 5, [6]]]
    expected = [6, 5, 4, 3, 2, 1]
    assert process_multi_dimensional_array(input_array) == expected