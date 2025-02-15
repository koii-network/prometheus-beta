import pytest
from src.array_reversal import reverse_array

def test_reverse_array_basic():
    """Test basic array reversal."""
    assert reverse_array([1, 2, 3]) == [3, 2, 1]

def test_reverse_array_empty():
    """Test reversing an empty array."""
    assert reverse_array([]) == []

def test_reverse_array_single_element():
    """Test reversing an array with a single element."""
    assert reverse_array([42]) == [42]

def test_reverse_array_mixed_types():
    """Test reversing an array with mixed types."""
    assert reverse_array([1, 'a', True, 3.14]) == [3.14, True, 'a', 1]

def test_reverse_array_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(None)