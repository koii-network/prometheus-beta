import pytest
import random
from src.bogosort import bogosort

def test_bogosort_basic_numeric_list():
    """Test sorting a basic numeric list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = bogosort(input_list)
    assert result == sorted(input_list)

def test_bogosort_already_sorted():
    """Test a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    result = bogosort(input_list)
    assert result == input_list

def test_bogosort_reverse_sorted():
    """Test a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    result = bogosort(input_list)
    assert result == sorted(input_list)

def test_bogosort_with_duplicates():
    """Test a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 3, 1]
    result = bogosort(input_list)
    assert result == sorted(input_list)

def test_bogosort_empty_list():
    """Test an empty list"""
    input_list = []
    result = bogosort(input_list)
    assert result == []

def test_bogosort_single_element():
    """Test a list with a single element"""
    input_list = [42]
    result = bogosort(input_list)
    assert result == input_list

def test_bogosort_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        bogosort("not a list")

def test_bogosort_uncomparable_elements():
    """Test raising ValueError for uncomparable elements"""
    with pytest.raises(ValueError):
        bogosort([1, 2, "a", 3])

def test_bogosort_random_list_length(random_seed=42):
    """Test sorting a randomly generated list of random length"""
    random.seed(random_seed)
    input_list = [random.randint(-1000, 1000) for _ in range(random.randint(1, 10))]
    result = bogosort(input_list)
    assert result == sorted(input_list)