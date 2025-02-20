import pytest
from src.check_increasing_sequence import is_valid_increasing_sequence

def test_empty_list():
    assert is_valid_increasing_sequence([]) == True

def test_single_element_list():
    assert is_valid_increasing_sequence([42]) == True

def test_valid_increasing_sequence():
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True

def test_invalid_not_increasing():
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False
    assert is_valid_increasing_sequence([1, 2, 2, 3, 4]) == False
    assert is_valid_increasing_sequence([1, 3, 2, 4]) == False

def test_negative_numbers():
    assert is_valid_increasing_sequence([-5, -3, -1, 0, 2]) == True
    assert is_valid_increasing_sequence([-1, -1, 0, 1]) == False

def test_non_integer_input():
    assert is_valid_increasing_sequence([1.5, 2.5, 3.5]) == False
    assert is_valid_increasing_sequence(['a', 'b', 'c']) == False

def test_type_error():
    with pytest.raises(TypeError):
        is_valid_increasing_sequence("not a list")
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(123)
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(None)