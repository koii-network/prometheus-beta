import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of an array."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Ensure shuffled array has same elements as original
    assert sorted(shuffled) == sorted(original)
    
    # Ensure shuffled array is not identical to original (with very high probability)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty array."""
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    """Test shuffling an array with a single element."""
    single_element = [42]
    assert shuffle_array(single_element) == single_element

def test_shuffle_array_type_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    with pytest.raises(TypeError):
        shuffle_array(123)
    with pytest.raises(TypeError):
        shuffle_array(None)

def test_shuffle_randomness(monkeypatch):
    """Test that the shuffle is random by mocking random.shuffle."""
    def mock_shuffle(lst):
        # Reverse the list to simulate a non-random shuffle
        lst.reverse()
    
    monkeypatch.setattr(random, 'shuffle', mock_shuffle)
    
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # With the mock, the list should be reversed
    assert shuffled == list(reversed(original))