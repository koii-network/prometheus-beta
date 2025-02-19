import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    indices = find_middle_range_indices(sorted_list)
    assert indices == [3, 4, 5]  # indices around mid value (5)

def test_even_length_list():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
    indices = find_middle_range_indices(sorted_list)
    assert indices == [3, 4]  # indices around mid value (4-5)

def test_custom_range_percentage():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    indices = find_middle_range_indices(sorted_list, range_percentage=0.5)
    assert indices == [2, 3, 4, 5, 6]

def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_middle_range_indices([])

def test_invalid_type_raises_error():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_middle_range_indices("not a list")

def test_invalid_range_percentage():
    with pytest.raises(ValueError, match="Range percentage must be a float between 0 and 1"):
        find_middle_range_indices([1, 2, 3], range_percentage=1.5)
        
def test_zero_range_percentage():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    indices = find_middle_range_indices(sorted_list, range_percentage=0)
    assert indices == [4]  # only the middle index