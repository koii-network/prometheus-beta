import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_array_basic():
    """Test that shuffle works with a basic list."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list contains same elements
    assert set(shuffled) == set(original)
    
    # Ensure shuffled list is not identical to original 
    # (though this might occasionally fail due to randomness)
    assert shuffled != original

def test_shuffle_array_different_types():
    """Test shuffle with different types of lists."""
    test_cases = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c', 'd'],
        [True, False, None],
        [1.1, 2.2, 3.3],
        []  # Empty list
    ]
    
    for case in test_cases:
        shuffled = shuffle_array(case)
        assert set(shuffled) == set(case)

def test_shuffle_array_not_modifying_original():
    """Ensure original list is not modified."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    assert original == [1, 2, 3, 4, 5]

def test_shuffle_array_type_error():
    """Test that TypeError is raised for non-list inputs."""
    invalid_inputs = [
        123,
        "string",
        {"key": "value"},
        (1, 2, 3),
        None
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError, match="Input must be a list"):
            shuffle_array(invalid_input)

def test_shuffle_array_randomness():
    """Test the randomness of shuffling."""
    original = list(range(10))
    
    # Run multiple shuffles and ensure they're not always the same
    shuffle_results = set()
    for _ in range(10):
        shuffle_results.add(tuple(shuffle_array(original)))
    
    # In a truly random shuffle, we expect multiple different arrangements
    assert len(shuffle_results) > 1