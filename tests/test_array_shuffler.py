import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_basic_list():
    """Test shuffling a basic list of integers."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list contains same elements
    assert set(shuffled) == set(original)
    
    # Ensure it's not the same order (unlikely to be identical after many runs)
    assert shuffled != original

def test_shuffle_different_types():
    """Test shuffling a list with different types of elements."""
    original = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list contains same elements
    assert set(shuffled) == set(original)
    
    # Ensure it's not the same order
    assert shuffled != original

def test_shuffle_empty_list():
    """Test shuffling an empty list."""
    original = []
    shuffled = shuffle_array(original)
    
    # Empty list remains empty
    assert shuffled == []

def test_shuffle_single_element_list():
    """Test shuffling a list with a single element."""
    original = [42]
    shuffled = shuffle_array(original)
    
    # Single element list remains unchanged
    assert shuffled == original

def test_shuffle_is_random():
    """Verify that multiple shuffles produce different results."""
    original = list(range(10))
    
    # Set a fixed seed for reproducibility of randomness test
    random.seed(42)
    
    # Collect multiple shuffle results
    shuffle_results = set()
    for _ in range(50):
        shuffled = shuffle_array(original)
        shuffle_results.add(tuple(shuffled))
    
    # Ensure multiple shuffles produce different arrangements
    assert len(shuffle_results) > 1

def test_invalid_input_type():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(None)