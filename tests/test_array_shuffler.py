import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of an array."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled array has same elements
    assert sorted(shuffled) == sorted(original)
    # Check that array is not in original order (with high probability)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty array."""
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    """Test shuffling an array with a single element."""
    single_element = [42]
    assert shuffle_array(single_element) == single_element

def test_shuffle_array_different_types():
    """Test shuffling an array with different types of elements."""
    mixed_array = [1, 'a', True, None, 3.14]
    shuffled = shuffle_array(mixed_array)
    
    # Check that shuffled array has same elements
    assert sorted(shuffled, key=str) == sorted(mixed_array, key=str)
    # Check that array is not in original order (with high probability)
    assert shuffled != mixed_array

def test_shuffle_array_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)
    
    with pytest.raises(TypeError):
        shuffle_array(None)