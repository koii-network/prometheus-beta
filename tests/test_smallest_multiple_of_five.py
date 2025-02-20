import pytest
from src.smallest_multiple_of_five import find_smallest_multiple_of_five

def test_basic_functionality():
    # Basic test cases
    assert find_smallest_multiple_of_five([1, 2, 3]) == 4
    assert find_smallest_multiple_of_five([3, 1, 2]) == 4
    assert find_smallest_multiple_of_five([10, 20]) == 5

def test_empty_array():
    assert find_smallest_multiple_of_five([]) == 5

def test_already_multiple_of_five():
    assert find_smallest_multiple_of_five([5, 10, 15]) == 5

def test_negative_numbers():
    assert find_smallest_multiple_of_five([-1, -2, -3]) == 3

def test_mixed_numbers():
    assert find_smallest_multiple_of_five([-10, 7, 3]) == 3

def test_type_error():
    with pytest.raises(TypeError):
        find_smallest_multiple_of_five("not a list")
    with pytest.raises(TypeError):
        find_smallest_multiple_of_five(123)

def test_value_error():
    with pytest.raises(ValueError):
        find_smallest_multiple_of_five([1, 2, "3"])
    with pytest.raises(ValueError):
        find_smallest_multiple_of_five([1.5, 2, 3])