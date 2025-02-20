import pytest
from src.multiply_array import multiply

def test_multiply_positive_numbers():
    assert multiply([1, 2, 3]) == [1, 4, 9]

def test_multiply_mixed_numbers():
    assert multiply([-1, 0, 2.5]) == [1, 0, 6.25]

def test_multiply_empty_list():
    assert multiply([]) == []

def test_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        multiply("not a list")

def test_invalid_input_non_numeric():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        multiply([1, 2, "three"])