import pytest
from src.symmetric_difference import find_symmetric_difference

def test_symmetric_difference_basic():
    """Test basic symmetric difference"""
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = find_symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 5, 6}

def test_symmetric_difference_empty_lists():
    """Test symmetric difference with empty lists"""
    list1 = []
    list2 = []
    result = find_symmetric_difference(list1, list2)
    assert result == []

def test_symmetric_difference_one_empty_list():
    """Test symmetric difference with one empty list"""
    list1 = [1, 2, 3]
    list2 = []
    result = find_symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 3}

def test_symmetric_difference_no_overlap():
    """Test symmetric difference with no overlapping elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = find_symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 3, 4, 5, 6}

def test_symmetric_difference_duplicate_elements():
    """Test symmetric difference with duplicate elements"""
    list1 = [1, 1, 2, 3]
    list2 = [3, 4, 4, 5]
    result = find_symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 4, 5}

def test_symmetric_difference_invalid_input_type():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        find_symmetric_difference("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError):
        find_symmetric_difference([1, 2, 3], "not a list")
    
    with pytest.raises(TypeError):
        find_symmetric_difference(None, [1, 2, 3])