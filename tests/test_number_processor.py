import pytest
from src.number_processor import process_number_array

def test_process_number_array_basic():
    # Basic test case
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = process_number_array(numbers)
    # Expected: 
    # Multiply 3rd, 6th, 9th numbers by 2 
    # Original even numbers to sum: 2, 4, 8
    assert result == 14

def test_process_number_array_empty():
    # Empty array should return 0
    numbers = []
    result = process_number_array(numbers)
    assert result == 0

def test_process_number_array_all_odd():
    # Array with only odd numbers
    numbers = [1, 3, 5, 7, 9]
    result = process_number_array(numbers)
    assert result == 0

def test_process_number_array_all_even():
    # Array with only even numbers
    numbers = [2, 4, 6, 8, 10]
    result = process_number_array(numbers)
    # 2, 4, 8 (10 would have been modified if it was at index 2)
    assert result == 14

def test_process_number_array_single_element():
    # Single element array
    numbers = [5]
    result = process_number_array(numbers)
    assert result == 0

def test_process_number_array_mixed():
    # Mixed array with various scenarios
    numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
    result = process_number_array(numbers)
    # Original even numbers to sum: 10, 30, 40, 50
    assert result == 130