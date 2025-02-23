import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_randomness():
    """
    Test that the shuffle function actually randomizes the array.
    """
    # Set a fixed seed for reproducibility
    random.seed(42)
    
    # Original array
    original = [1, 2, 3, 4, 5]
    
    # Perform multiple shuffles
    shuffles = [shuffle_array(original.copy()) for _ in range(10)]
    
    # Check that not all shuffles are the same
    assert any(shuffle != original for shuffle in shuffles), "Shuffles should not always be the same"

def test_shuffle_array_same_elements():
    """
    Test that the shuffled array contains the same elements as the original.
    """
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check length
    assert len(shuffled) == len(original), "Shuffled array should have same length"
    
    # Check that all original elements are present
    assert sorted(shuffled) == sorted(original), "Shuffled array should contain same elements"

def test_shuffle_empty_array():
    """
    Test shuffling an empty array.
    """
    empty_list = []
    shuffled = shuffle_array(empty_list)
    assert shuffled == [], "Shuffling an empty list should return an empty list"

def test_shuffle_single_element_array():
    """
    Test shuffling an array with a single element.
    """
    single_element = [42]
    shuffled = shuffle_array(single_element)
    assert shuffled == [42], "Shuffling a single-element list should return the same list"

def test_shuffle_preserves_original():
    """
    Test that the original array is not modified.
    """
    original = [1, 2, 3, 4, 5]
    _ = shuffle_array(original)
    assert original == [1, 2, 3, 4, 5], "Original array should not be modified"

def test_shuffle_different_types():
    """
    Test shuffling an array with different types of elements.
    """
    mixed_array = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(mixed_array)
    
    # Check length
    assert len(shuffled) == len(mixed_array), "Shuffled array should have same length"
    
    # Check that all original elements are present
    assert sorted(shuffled, key=str) == sorted(mixed_array, key=str), "Shuffled array should contain same elements"

def test_invalid_input_type():
    """
    Test that a TypeError is raised for non-list inputs.
    """
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(None)