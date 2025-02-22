import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of an array"""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled array contains same elements
    assert sorted(shuffled) == sorted(original)
    
    # Check that the order is different (with high probability)
    assert shuffled != original

def test_shuffle_array_different_types():
    """Test shuffling arrays with different types of elements"""
    test_cases = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c', 'd'],
        [1, 'a', True, 3.14],
        []
    ]
    
    for case in test_cases:
        shuffled = shuffle_array(case)
        assert sorted(shuffled) == sorted(case)
        assert len(shuffled) == len(case)

def test_shuffle_array_non_list_input():
    """Test that non-list inputs raise a TypeError"""
    invalid_inputs = [
        "not a list",
        123,
        None,
        (1, 2, 3),
        {"key": "value"}
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError, match="Input must be a list"):
            shuffle_array(invalid_input)

def test_shuffle_array_randomness():
    """Test that shuffling produces different orders with high probability"""
    original = list(range(10))
    
    # Try multiple shuffles and track if any keep the original order
    different_order_count = 0
    num_tries = 50
    
    for _ in range(num_tries):
        shuffled = shuffle_array(original)
        if shuffled != original:
            different_order_count += 1
    
    # Statistically, it's extremely unlikely to get the same order every time
    assert different_order_count > num_tries * 0.8