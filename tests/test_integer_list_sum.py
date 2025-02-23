import pytest
from src.integer_list_sum import sum_integers

def test_sum_normal_list():
    """Test summing a list of positive and negative integers."""
    assert sum_integers([1, 2, 3, 4, 5]) == 15
    assert sum_integers([-1, -2, -3]) == -6
    assert sum_integers([10, -5, 3]) == 8

def test_empty_list():
    """Test summing an empty list."""
    assert sum_integers([]) == 0

def test_single_element_list():
    """Test summing a list with a single element."""
    assert sum_integers([42]) == 42

def test_large_list():
    """Test summing a large list of integers."""
    large_list = list(range(1, 1001))
    assert sum_integers(large_list) == sum(large_list)

def test_invalid_input_type():
    """Test raising TypeError for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers("not a list")

def test_invalid_list_elements():
    """Test raising TypeError for lists with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1.5, 2, 3])
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, None, 3])