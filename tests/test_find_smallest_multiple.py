import pytest
from src.find_smallest_multiple import find_smallest_multiple_of_five

def test_basic_cases():
    assert find_smallest_multiple_of_five([1, 2, 3]) == 4
    assert find_smallest_multiple_of_five([3, 1, 2]) == 4
    assert find_smallest_multiple_of_five([10, 20]) == 5

def test_empty_list():
    assert find_smallest_multiple_of_five([]) == 5

def test_already_multiple_of_five():
    assert find_smallest_multiple_of_five([5, 10]) == 5

def test_large_numbers():
    assert find_smallest_multiple_of_five([1000, 2000]) == 5

def test_negative_numbers():
    assert find_smallest_multiple_of_five([-3, -1, -2]) == 1

def test_input_validation():
    with pytest.raises(TypeError):
        find_smallest_multiple_of_five(123)
    
    with pytest.raises(TypeError):
        find_smallest_multiple_of_five("not a list")
    
    with pytest.raises(ValueError):
        find_smallest_multiple_of_five([1, 2, "3"])
    
    with pytest.raises(ValueError):
        find_smallest_multiple_of_five([1, 2, 3.5])