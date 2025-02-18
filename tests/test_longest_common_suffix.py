import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_common_suffix_multiple_strings():
    """Test finding a common suffix in multiple strings"""
    result = find_longest_common_suffix(["flower", "power", "tower"])
    assert result == "ower"

def test_single_string():
    """Test a list with a single string returns the whole string"""
    result = find_longest_common_suffix(["hello"])
    assert result == "hello"

def test_empty_list():
    """Test an empty list returns an empty string"""
    result = find_longest_common_suffix([])
    assert result == ""

def test_no_common_suffix():
    """Test strings with no common suffix"""
    result = find_longest_common_suffix(["cat", "dog", "bird"])
    assert result == ""

def test_full_common_suffix():
    """Test when strings have a full common suffix"""
    result = find_longest_common_suffix(["pattern", "pattern"])
    assert result == "pattern"

def test_partial_common_suffix():
    """Test a partial common suffix"""
    result = find_longest_common_suffix(["calendar", "solar", "polar"])
    assert result == "lar"

def test_invalid_input_non_list():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_invalid_input_non_string_elements():
    """Test list with non-string elements raises TypeError"""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["valid", 123, "invalid"])

def test_empty_strings():
    """Test list with empty strings"""
    result = find_longest_common_suffix(["", "", ""])
    assert result == ""