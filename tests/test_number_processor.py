import pytest
from src.number_processor import process_number_array

def test_basic_processing():
    # Test standard case
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Expected: Sum of even numbers, skipping modified 3rd numbers
    # Modified 3rd numbers: 3*2=6, 6*2=12
    # Even numbers to sum: 2, 4, 8, 10
    assert process_number_array(numbers) == 24

def test_empty_list():
    # Test empty list returns 0
    assert process_number_array([]) == 0

def test_no_even_numbers():
    # Test list with no even numbers
    assert process_number_array([1, 3, 5, 7, 9]) == 0

def test_all_even_numbers():
    # Test list with all even numbers
    numbers = [2, 4, 6, 8, 10, 12]
    # Modified 3rd numbers: 6*2=12
    # Even numbers to sum: 2, 4, 8, 10
    assert process_number_array(numbers) == 24

def test_invalid_input():
    # Test invalid input type
    with pytest.raises(TypeError):
        process_number_array("not a list")

def test_single_number_list():
    # Test list with single number
    assert process_number_array([5]) == 0

def test_minimal_even_numbers():
    # Test list with minimal even numbers
    numbers = [1, 2, 6, 4, 5, 12]
    # Modified 3rd numbers: 6*2=12
    # Even numbers to sum: 2, 4
    assert process_number_array(numbers) == 6