import pytest
from src.triangular_numbers import count_triangular_numbers

def test_count_triangular_numbers():
    # Test some known triangular number counts
    assert count_triangular_numbers(0) == 0
    assert count_triangular_numbers(1) == 1
    assert count_triangular_numbers(5) == 2
    assert count_triangular_numbers(10) == 3
    assert count_triangular_numbers(15) == 4

def test_larger_numbers():
    assert count_triangular_numbers(100) == 13
    assert count_triangular_numbers(1000) == 44

def test_input_validation():
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_triangular_numbers(-5)
    
    # Test non-integer input
    with pytest.raises(ValueError, match="Input must be an integer"):
        count_triangular_numbers(3.14)
    with pytest.raises(ValueError, match="Input must be an integer"):
        count_triangular_numbers("10")

def test_triangular_numbers_sequence():
    # Verify the actual triangular numbers
    expected_triangular_nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
    
    # Verify that we get the correct count of triangular numbers
    for i, max_num in enumerate(expected_triangular_nums[1:], start=1):
        assert count_triangular_numbers(max_num) == i