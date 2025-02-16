import pytest
from src.string_sorter import sort_strings_by_length

def test_sort_strings_by_length_basic():
    """Test basic sorting of strings by length"""
    input_list = ["a", "ccc", "bb"]
    expected = ["a", "bb", "ccc"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_empty_list():
    """Test sorting an empty list"""
    assert sort_strings_by_length([]) == []

def test_sort_strings_by_length_same_length():
    """Test sorting strings of the same length"""
    input_list = ["cat", "dog", "rat"]
    expected = ["cat", "dog", "rat"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_mixed_case():
    """Test sorting strings with mixed case"""
    input_list = ["Python", "java", "C++", "Ruby"]
    expected = ["C++", "java", "Ruby", "Python"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_invalid_input_non_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_strings_by_length("not a list")

def test_sort_strings_by_length_invalid_input_non_strings():
    """Test raising TypeError for list with non-string elements"""
    with pytest.raises(TypeError, match="All elements in the list must be strings"):
        sort_strings_by_length([1, 2, 3])
        
def test_sort_strings_by_length_mixed_types():
    """Test raising TypeError for list with mixed types"""
    with pytest.raises(TypeError, match="All elements in the list must be strings"):
        sort_strings_by_length(["hello", 42, "world"])