import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test that shuffle_array returns a list with same elements."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    assert len(shuffled) == len(original)
    assert sorted(shuffled) == sorted(original)
    assert shuffled != original  # High probability of different order

def test_shuffle_array_randomness():
    """Test the randomness of shuffling multiple times."""
    original = [1, 2, 3, 4, 5]
    
    # Set a random seed for reproducibility of this test
    random.seed(42)
    shuffle1 = shuffle_array(original)
    
    random.seed(42)
    shuffle2 = shuffle_array(original)
    
    # These should be the same due to same seed
    assert shuffle1 == shuffle2

def test_shuffle_array_empty_list():
    """Test shuffling an empty list."""
    original = []
    shuffled = shuffle_array(original)
    assert shuffled == []

def test_shuffle_array_single_element():
    """Test shuffling a list with a single element."""
    original = [42]
    shuffled = shuffle_array(original)
    assert shuffled == [42]

def test_shuffle_array_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(None)

def test_shuffle_array_preserves_original():
    """Test that the original list is not modified."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    assert original == [1, 2, 3, 4, 5]  # Original list unchanged
    assert shuffled is not original  # Different list object