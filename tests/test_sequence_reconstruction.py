import pytest
from src.sequence_reconstruction import min_sequence_reconstruction

def test_basic_sequence_transformation():
    """Test basic sequence transformation."""
    original = [1, 2, 3, 4, 5]
    current = [1, 2, 6, 4, 5]
    assert min_sequence_reconstruction(original, current) == 1

def test_complete_different_sequences():
    """Test sequences with no common elements."""
    original = [1, 2, 3]
    current = [4, 5, 6]
    assert min_sequence_reconstruction(original, current) == 6

def test_identical_sequences():
    """Test identical sequences."""
    original = [1, 2, 3, 4]
    current = [1, 2, 3, 4]
    assert min_sequence_reconstruction(original, current) == 0

def test_empty_original_sequence():
    """Test when original sequence is empty."""
    original = []
    current = [1, 2, 3]
    assert min_sequence_reconstruction(original, current) == 3

def test_empty_current_sequence():
    """Test when current sequence is empty."""
    original = [1, 2, 3]
    current = []
    assert min_sequence_reconstruction(original, current) == 3

def test_none_input_raises_error():
    """Test that None inputs raise ValueError."""
    with pytest.raises(ValueError):
        min_sequence_reconstruction(None, [1, 2, 3])
    
    with pytest.raises(ValueError):
        min_sequence_reconstruction([1, 2, 3], None)

def test_non_list_input_raises_error():
    """Test that non-list inputs raise ValueError."""
    with pytest.raises(ValueError):
        min_sequence_reconstruction("not a list", [1, 2, 3])
    
    with pytest.raises(ValueError):
        min_sequence_reconstruction([1, 2, 3], "not a list")

def test_duplicate_elements():
    """Test sequences with duplicate elements."""
    original = [1, 1, 2, 3, 3]
    current = [1, 2, 2, 4]
    assert min_sequence_reconstruction(original, current) == 3