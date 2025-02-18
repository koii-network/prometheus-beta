import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_normal_case():
    """Test with a standard list of strings with a common prefix"""
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_no_common_prefix():
    """Test with strings having no common prefix"""
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_single_string():
    """Test with a single string"""
    assert find_longest_common_prefix(["alone"]) == "alone"

def test_empty_list():
    """Test with an empty list"""
    assert find_longest_common_prefix([]) == ""

def test_all_strings_identical():
    """Test with identical strings"""
    assert find_longest_common_prefix(["abc", "abc", "abc"]) == "abc"

def test_prefix_whole_string():
    """Test where one string is the prefix of all others"""
    assert find_longest_common_prefix(["apple", "apricot", "app"]) == "ap"

def test_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError):
        find_longest_common_prefix("not a list")

def test_invalid_list_element_type():
    """Test handling of list with non-string elements"""
    with pytest.raises(TypeError):
        find_longest_common_prefix(["string", 123, "another"])