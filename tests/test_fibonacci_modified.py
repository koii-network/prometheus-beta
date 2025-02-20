import pytest
from src.fibonacci_modified import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    # Test basic functionality
    result = generate_modified_fibonacci(5)
    assert len(result) == 5
    assert result == [1, 1, 2, 3, 5]

def test_generate_modified_fibonacci_divisibility():
    # Test divisibility constraint
    result = generate_modified_fibonacci(6)
    assert len(result) == 6
    
    # Check that sum of consecutive numbers (from 3rd onwards) is divisible by 3
    for i in range(2, len(result)):
        assert (result[i-1] + result[i]) % 3 == 0

def test_generate_modified_fibonacci_invalid_input():
    # Test invalid inputs
    with pytest.raises(ValueError):
        generate_modified_fibonacci(0)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci(1.5)

def test_generate_modified_fibonacci_edge_cases():
    # Test single element cases
    assert generate_modified_fibonacci(1) == [1]
    assert generate_modified_fibonacci(2) == [1, 1]

def test_generate_modified_fibonacci_larger_sequence():
    # Test a larger sequence to ensure constraint holds
    result = generate_modified_fibonacci(10)
    assert len(result) == 10
    
    # Verify divisibility for entire sequence
    for i in range(2, len(result)):
        assert (result[i-1] + result[i]) % 3 == 0, f"Failed at index {i}"