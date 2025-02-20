import pytest
from src.multi_array_processor import process_multi_dimensional_array

def test_full_processing_scenario():
    # Test basic scenario with multi-dimensional array
    input_array = [[1, 2, 3], [], [4, 5], [6, 7, 8]]
    expected_output = [8, 7, 6, 5, 4, 3, 2, 1]
    assert process_multi_dimensional_array(input_array) == expected_output

def test_array_with_duplicates():
    # Test scenario with duplicate elements
    input_array = [[1, 2, 2], [3, 3, 4], [5, 5, 5]]
    expected_output = [2, 1, 4, 3, 5]
    assert process_multi_dimensional_array(input_array) == expected_output

def test_all_empty_arrays():
    # Test scenario with all empty arrays
    input_array = [[], [], []]
    expected_output = []
    assert process_multi_dimensional_array(input_array) == expected_output

def test_mixed_data_types():
    # Test scenario with mixed data types
    input_array = [[1, 'a'], ['b', 2], [3, 'c'], ['a', 1]]
    expected_output = ['c', 3, 2, 'b', 'a', 1]
    assert process_multi_dimensional_array(input_array) == expected_output

def test_nested_arrays():
    # Test scenario with nested arrays (not flattened beyond one level)
    input_array = [[1, [2, 3]], [4, 5], [[6], 7]]
    expected_output = [7, 6, 5, 4, 3, 2, 1]
    assert process_multi_dimensional_array(input_array) == expected_output