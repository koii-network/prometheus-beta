import pytest
from src.array_reversal import reverse_array

def test_reverse_array_basic():
    # Test basic array reversal
    assert reverse_array([1, 2, 3]) == [3, 2, 1]
    assert reverse_array(['a', 'b', 'c']) == ['c', 'b', 'a']

def test_reverse_array_empty():
    # Test empty array
    assert reverse_array([]) == []

def test_reverse_array_single_element():
    # Test array with single element
    assert reverse_array([42]) == [42]

def test_reverse_array_mixed_types():
    # Test array with mixed types
    assert reverse_array([1, 'two', 3.0]) == [3.0, 'two', 1]

def test_reverse_array_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        reverse_array("not a list")
    with pytest.raises(TypeError):
        reverse_array(123)
    with pytest.raises(TypeError):
        reverse_array(None)