import pytest
from src.array_reversal import reverse_array

def test_reverse_empty_list():
    assert reverse_array([]) == []

def test_reverse_single_element_list():
    assert reverse_array([42]) == [42]

def test_reverse_multiple_elements():
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_reverse_mixed_types():
    assert reverse_array([1, 'a', True, 3.14]) == [3.14, True, 'a', 1]

def test_reverse_invalid_input():
    with pytest.raises(TypeError):
        reverse_array("not a list")
    
    with pytest.raises(TypeError):
        reverse_array(123)
    
    with pytest.raises(TypeError):
        reverse_array(None)