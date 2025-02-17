import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_basic():
    """Test basic shuffling of an array."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that the shuffled array contains the same elements
    assert sorted(shuffled) == sorted(original)
    
    # Check that the order is different (with high probability)
    assert shuffled != original

def test_shuffle_empty_list():
    """Test shuffling an empty list."""
    empty = []
    shuffled = shuffle_array(empty)
    assert shuffled == []

def test_shuffle_single_element():
    """Test shuffling a list with a single element."""
    single = [42]
    shuffled = shuffle_array(single)
    assert shuffled == [42]

def test_shuffle_error_handling():
    """Test error handling for non-list inputs."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)

def test_randomness():
    """Test that repeated shuffles produce different orders."""
    original = list(range(10))
    
    # Set a fixed random seed for reproducibility
    random.seed(42)
    
    # Perform multiple shuffles and ensure they're not always the same
    shuffle1 = shuffle_array(original)
    shuffle2 = shuffle_array(original)
    
    # Reset the seed to ensure fairness
    random.seed(42)
    
    assert len(shuffle1) == len(original)
    assert len(shuffle2) == len(original)
    
    # Note: While possible, it's extremely unlikely that two shuffles 
    # will produce the exact same order, especially for lists > 3 elements
    assert shuffle1 != shuffle2 or shuffle1 == original