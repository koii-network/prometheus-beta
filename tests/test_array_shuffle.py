import pytest
from src.array_shuffle import shuffle_array
import random

def test_shuffle_array_basic():
    # Test basic shuffling
    input_list = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(input_list)
    
    # Check that shuffled list contains same elements
    assert sorted(shuffled) == sorted(input_list)
    
    # Check that shuffled list is not in original order (with high probability)
    assert shuffled != input_list

def test_shuffle_array_empty():
    # Test empty list
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    # Test single element list
    single_list = [42]
    assert shuffle_array(single_list) == single_list

def test_shuffle_array_different_types():
    # Test list with different types of elements
    mixed_list = [1, 'a', True, None, 3.14]
    shuffled = shuffle_array(mixed_list)
    
    # Check that shuffled list contains same elements
    assert sorted(shuffled) == sorted(mixed_list)

def test_shuffle_array_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)
    
    with pytest.raises(TypeError):
        shuffle_array(None)

def test_shuffle_randomness():
    # Test randomness by running multiple shuffles and checking they're not always the same
    input_list = list(range(10))
    
    # Set a seed for reproducibility of the randomness test
    random.seed(42)
    attempts = 10
    shuffled_results = set()
    
    for _ in range(attempts):
        shuffled = tuple(shuffle_array(input_list))
        shuffled_results.add(shuffled)
    
    # Ensure we have multiple different shuffles
    assert len(shuffled_results) > 1