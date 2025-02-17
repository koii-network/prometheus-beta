import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_basic():
    """Test basic shuffling of a list"""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Verify the shuffled list contains the same elements
    assert set(shuffled) == set(original)
    
    # Verify the list is not in the original order (unlikely to be the same)
    assert shuffled != original

def test_shuffle_empty_list():
    """Test shuffling an empty list"""
    original = []
    shuffled = shuffle_array(original)
    assert shuffled == []

def test_shuffle_single_element():
    """Test shuffling a list with a single element"""
    original = [42]
    shuffled = shuffle_array(original)
    assert shuffled == [42]

def test_shuffle_raises_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(None)

def test_shuffle_randomness():
    """Test that multiple shuffles can produce different arrangements"""
    original = [1, 2, 3, 4, 5]
    
    # Set a fixed seed for reproducibility of randomness test
    random.seed(42)
    
    # Generate multiple shuffles
    shuffles = [shuffle_array(original) for _ in range(10)]
    
    # At least some shuffles should be different
    assert len(set(tuple(shuffle) for shuffle in shuffles)) > 1