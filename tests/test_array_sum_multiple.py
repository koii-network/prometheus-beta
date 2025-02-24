import pytest
from src.array_sum_multiple import find_smallest_int_to_multiple_of_five

def test_basic_scenarios():
    assert find_smallest_int_to_multiple_of_five([1, 2, 3, 4]) == 5
    assert find_smallest_int_to_multiple_of_five([3, 1, 2]) == 4
    assert find_smallest_int_to_multiple_of_five([1]) == 4
    assert find_smallest_int_to_multiple_of_five([]) == 5

def test_edge_cases():
    assert find_smallest_int_to_multiple_of_five([5]) == 5
    assert find_smallest_int_to_multiple_of_five([10, 15]) == 5

def test_error_handling():
    with pytest.raises(TypeError):
        find_smallest_int_to_multiple_of_five("not a list")
    
    with pytest.raises(TypeError):
        find_smallest_int_to_multiple_of_five(None)
    
    with pytest.raises(ValueError):
        find_smallest_int_to_multiple_of_five([1, 2, '3'])
    
    with pytest.raises(ValueError):
        find_smallest_int_to_multiple_of_five([1, 2, 3.5])

def test_negative_numbers():
    assert find_smallest_int_to_multiple_of_five([-1, -2, -3]) == 1
    assert find_smallest_int_to_multiple_of_five([-5, -10]) == 5

def test_large_numbers():
    assert find_smallest_int_to_multiple_of_five([1000000, 2000000]) == 5