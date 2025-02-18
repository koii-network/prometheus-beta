import pytest
from src.string_sorter import sort_strings_by_length

def test_sort_strings_by_length_basic():
    """Test basic string length sorting."""
    input_list = ["a", "abc", "ab"]
    expected = ["a", "ab", "abc"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_empty():
    """Test sorting an empty list."""
    assert sort_strings_by_length([]) == []

def test_sort_strings_by_length_same_length():
    """Test sorting strings of the same length."""
    input_list = ["cat", "dog", "rat"]
    assert sort_strings_by_length(input_list) == ["cat", "dog", "rat"]

def test_sort_strings_by_length_mixed_lengths():
    """Test sorting a list with mixed string lengths."""
    input_list = ["python", "java", "c", "rust", "go"]
    expected = ["c", "go", "java", "rust", "python"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_invalid_input_not_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_strings_by_length("not a list")

def test_sort_strings_by_length_invalid_input_non_strings():
    """Test raising TypeError for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        sort_strings_by_length(["valid", 123, "invalid"])