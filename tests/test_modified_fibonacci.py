import pytest
from src.modified_fibonacci import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    """Test basic functionality of the modified Fibonacci sequence"""
    result = generate_modified_fibonacci(5)
    assert result == [0, 1, 2, 4, 6]
    
    # Verify that the sum of consecutive numbers is always odd
    for i in range(1, len(result)):
        assert (result[i-1] + result[i]) % 2 == 1

def test_generate_modified_fibonacci_single_element():
    """Test generating a single element in the sequence"""
    result = generate_modified_fibonacci(1)
    assert result == [0]

def test_generate_modified_fibonacci_two_elements():
    """Test generating two elements in the sequence"""
    result = generate_modified_fibonacci(2)
    assert result == [0, 1]

def test_generate_modified_fibonacci_longer_sequence():
    """Test a longer sequence to ensure consistent odd sum rule"""
    result = generate_modified_fibonacci(10)
    
    # Verify that the sum of consecutive numbers is always odd
    for i in range(1, len(result)):
        assert (result[i-1] + result[i]) % 2 == 1

def test_generate_modified_fibonacci_invalid_input():
    """Test that the function raises a ValueError for invalid input"""
    with pytest.raises(ValueError):
        generate_modified_fibonacci(0)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)