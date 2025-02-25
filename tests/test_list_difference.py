import pytest
from src.list_difference import find_list_difference

def test_basic_list_difference():
    """Test finding differences between two simple lists."""
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    
    result = find_list_difference(list1, list2)
    
    assert result == {
        'added': [5, 6],
        'removed': [1, 2],
        'unchanged': [3, 4]
    }

def test_identical_lists():
    """Test when both lists are identical."""
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    
    result = find_list_difference(list1, list2)
    
    assert result == {
        'added': [],
        'removed': [],
        'unchanged': [1, 2, 3]
    }

def test_completely_different_lists():
    """Test when lists have no common elements."""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    result = find_list_difference(list1, list2)
    
    assert result == {
        'added': [4, 5, 6],
        'removed': [1, 2, 3],
        'unchanged': []
    }

def test_empty_lists():
    """Test with empty lists."""
    list1 = []
    list2 = []
    
    result = find_list_difference(list1, list2)
    
    assert result == {
        'added': [],
        'removed': [],
        'unchanged': []
    }

def test_one_empty_list():
    """Test when one list is empty."""
    list1 = [1, 2, 3]
    list2 = []
    
    result = find_list_difference(list1, list2)
    
    assert result == {
        'added': [],
        'removed': [1, 2, 3],
        'unchanged': []
    }

def test_lists_with_duplicates():
    """Test lists with duplicate elements."""
    list1 = [1, 1, 2, 3, 3]
    list2 = [1, 2, 2, 4, 4]
    
    result = find_list_difference(list1, list2)
    
    assert result == {
        'added': [4],
        'removed': [3],
        'unchanged': [1, 2]
    }

def test_invalid_input_type():
    """Test raising TypeError for non-list inputs."""
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        find_list_difference("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        find_list_difference([1, 2, 3], "not a list")
    
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        find_list_difference(None, None)