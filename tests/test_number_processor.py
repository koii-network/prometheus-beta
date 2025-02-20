import pytest
from src.number_processor import process_number_array

def test_process_number_array_basic():
    # Basic test case
    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Expected: 
    # Every third number is multiplied by 2: [1, 2, 6, 4, 5, 12, 7, 8, 18, 10]
    # Even numbers to sum: 2, 4, 8, 10 (excluding 6, 12, 18 which are modified)
    assert process_number_array(input_array) == 24

def test_process_number_array_empty():
    # Test with empty array
    assert process_number_array([]) == 0

def test_process_number_array_all_odd():
    # Test with all odd numbers
    input_array = [1, 3, 5, 7, 9, 11]
    assert process_number_array(input_array) == 0

def test_process_number_array_all_even():
    # Test with all even numbers
    input_array = [2, 4, 6, 8, 10, 12]
    # Expected: 
    # Every third number is multiplied by 2
    # Even numbers to sum: 2, 4, 8, 10
    assert process_number_array(input_array) == 24

def test_process_number_array_single_element():
    # Test with single element
    assert process_number_array([5]) == 0
    assert process_number_array([6]) == 6

def test_process_number_array_negative_numbers():
    # Test with negative numbers
    input_array = [-1, -2, -3, -4, -5, -6]
    # Expected: 
    # Every third number is multiplied by 2
    # Even numbers to sum: -2, -4
    assert process_number_array(input_array) == -6