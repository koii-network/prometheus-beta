import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of a list of integers."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Assert that:
    # 1. The shuffled list contains the same elements
    # 2. The shuffled list is not exactly the same as the original
    assert sorted(shuffled) == sorted(original)
    assert shuffled != original

def test_shuffle_array_empty_list():
    """Test shuffling an empty list."""
    empty_list = []
    shuffled = shuffle_array(empty_list)
    assert shuffled == []

def test_shuffle_array_single_element():
    """Test shuffling a list with a single element."""
    single_element = [42]
    shuffled = shuffle_array(single_element)
    assert shuffled == [42]

def test_shuffle_array_different_types():
    """Test shuffling a list with different types of elements."""
    mixed_list = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(mixed_list)
    
    # Assert that:
    # 1. The shuffled list contains the same elements
    # 2. The shuffled list is not exactly the same as the original
    assert sorted(shuffled, key=str) == sorted(mixed_list, key=str)
    assert shuffled != mixed_list

def test_shuffle_array_type_error():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)

def test_shuffle_array_randomness():
    """Test the randomness of the shuffle function.
    
    This test checks that shuffling multiple times produces different results 
    with high probability.
    """
    original = list(range(10))
    shuffles = [shuffle_array(original) for _ in range(100)]
    
    # Ensure at least some shuffles are different from the original
    different_shuffles = [s for s in shuffles if s != original]
    assert len(different_shuffles) > 0