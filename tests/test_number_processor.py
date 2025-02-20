import pytest
from src.number_processor import process_number_array

def test_process_number_array_basic():
    """Test basic functionality of the number processing function"""
    assert process_number_array([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 16

def test_process_number_array_empty():
    """Test processing an empty array"""
    assert process_number_array([]) == 0

def test_process_number_array_no_evens():
    """Test array with no even numbers"""
    assert process_number_array([1, 3, 5, 7, 9]) == 0

def test_process_number_array_all_even():
    """Test array with all even numbers"""
    assert process_number_array([2, 4, 6, 8, 10]) == 16

def test_process_number_array_negative_numbers():
    """Test array with negative numbers"""
    assert process_number_array([-2, 3, -4, 5, -6, 7, -8, 9, -10]) == -16