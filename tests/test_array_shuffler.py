import pytest
from src.array_shuffler import shuffle_array
import random

def test_shuffle_array_basic():
    """Test basic shuffling of an array."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled array has same elements
    assert sorted(shuffled) == sorted(original)
    
    # Check that the order is different (with high probability)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty array."""
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    """Test shuffling an array with a single element."""
    single_element = [42]
    assert shuffle_array(single_element) == single_element

def test_shuffle_array_type_error():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    with pytest.raises(TypeError):
        shuffle_array(123)

def test_shuffle_randomness():
    """Test that multiple shuffles produce different orders."""
    original = list(range(10))
    random.seed(42)  # Set seed for reproducibility
    
    shuffle1 = shuffle_array(original)
    shuffle2 = shuffle_array(original)
    
    # With high probability, shuffles will be different
    assert shuffle1 != shuffle2