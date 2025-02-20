import pytest
from src.fibonacci_mod_three import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    # Test basic sequence generation
    result = generate_modified_fibonacci(5)
    assert len(result) == 5
    assert result[0] == 1
    assert result[1] == 1

def test_consecutive_sum_divisible_by_three():
    # Test that sum of consecutive numbers is divisible by 3
    result = generate_modified_fibonacci(10)
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, \
            f"Sum of {result[i-2]} and {result[i-1]} is not divisible by 3"

def test_small_sequences():
    # Test sequences of length 1 and 2
    assert generate_modified_fibonacci(1) == [1]
    assert generate_modified_fibonacci(2) == [1, 1]

def test_invalid_input():
    # Test invalid input
    with pytest.raises(ValueError):
        generate_modified_fibonacci(0)
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)

def test_sequence_properties():
    # Additional tests for sequence properties
    result = generate_modified_fibonacci(7)
    assert len(result) == 7
    
    # Verify that each pair of consecutive numbers satisfies the condition
    for i in range(2, len(result)):
        assert (result[i-2] + result[i-1]) % 3 == 0, \
            f"Failed at index {i}: {result[i-2]} + {result[i-1]} not divisible by 3"