import pytest
from src.fibonacci_divisible import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    # Test basic sequence generation
    assert generate_modified_fibonacci(1) == [1]
    assert generate_modified_fibonacci(2) == [1, 1]
    
    # Test first few numbers of the unique sequence
    result = generate_modified_fibonacci(5)
    assert len(result) == 5
    
    # Check the divisibility by 3 constraint
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, \
            f"Sum of {result[i-2]} and {result[i-1]} is not divisible by 3"

def test_generate_modified_fibonacci_larger_sequence():
    # Test a larger sequence
    result = generate_modified_fibonacci(10)
    assert len(result) == 10
    
    # Check the divisibility by 3 constraint
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, \
            f"Sum of {result[i-2]} and {result[i-1]} is not divisible by 3"

def test_generate_modified_fibonacci_error_handling():
    # Test invalid inputs
    with pytest.raises(ValueError):
        generate_modified_fibonacci(0)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci(1.5)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci("string")