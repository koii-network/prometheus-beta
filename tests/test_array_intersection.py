import pytest
from src.array_intersection import find_array_intersection

def test_basic_intersection():
    """Test basic intersection of two arrays"""
    assert find_array_intersection([1, 2, 3], [3, 4, 5]) == [3]

def test_multiple_intersections():
    """Test intersection with multiple common elements"""
    assert find_array_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_no_intersection():
    """Test arrays with no common elements"""
    assert find_array_intersection([1, 2], [3, 4]) == []

def test_duplicate_handling():
    """Test handling of duplicate elements"""
    assert find_array_intersection([1, 1, 2, 2], [2, 2, 3, 3]) == [2]

def test_empty_arrays():
    """Test intersection with empty arrays"""
    assert find_array_intersection([], [1, 2, 3]) == []
    assert find_array_intersection([1, 2, 3], []) == []

def test_invalid_input_type():
    """Test error handling for non-list inputs"""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        find_array_intersection("not a list", [1, 2, 3])
    with pytest.raises(TypeError, match="Inputs must be lists"):
        find_array_intersection([1, 2, 3], "not a list")

def test_non_integer_elements():
    """Test error handling for non-integer elements"""
    with pytest.raises(TypeError, match="All array elements must be integers"):
        find_array_intersection([1, 2, "3"], [3, 4, 5])
    with pytest.raises(TypeError, match="All array elements must be integers"):
        find_array_intersection([1, 2, 3], [3, 4, "5"])

def test_large_arrays():
    """Test intersection with larger arrays"""
    arr1 = list(range(1000))
    arr2 = list(range(500, 1500))
    expected = list(range(500, 1000))
    assert find_array_intersection(arr1, arr2) == expected