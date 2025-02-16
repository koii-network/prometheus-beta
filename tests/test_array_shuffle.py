import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_array_basic():
    """Test that shuffle_array returns a list with the same elements."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list has same length
    assert len(shuffled) == len(original)
    
    # Check that all original elements are present
    assert sorted(shuffled) == sorted(original)

def test_shuffle_array_randomness():
    """Test that shuffle_array produces different arrangements."""
    # Set a fixed seed to make the test reproducible
    random.seed(42)
    
    original = [1, 2, 3, 4, 5]
    results = set()
    
    # Run multiple shuffles to check for randomness
    for _ in range(20):
        shuffled = shuffle_array(original)
        results.add(tuple(shuffled))
    
    # Ensure multiple unique arrangements are generated
    assert len(results) > 1

def test_shuffle_array_empty_list():
    """Test shuffling an empty list."""
    empty_list = []
    shuffled = shuffle_array(empty_list)
    assert shuffled == []

def test_shuffle_array_single_element():
    """Test shuffling a list with a single element."""
    single_element_list = [42]
    shuffled = shuffle_array(single_element_list)
    assert shuffled == [42]

def test_shuffle_array_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(None)