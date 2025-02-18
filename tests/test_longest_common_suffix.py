import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_basic_common_suffix():
    assert find_longest_common_suffix(["flower", "bower", "power"]) == "wer"

def test_single_string():
    assert find_longest_common_suffix(["hello"]) == "hello"

def test_no_common_suffix():
    assert find_longest_common_suffix(["abc", "def", "ghi"]) == ""

def test_same_strings():
    assert find_longest_common_suffix(["cat", "cat", "cat"]) == "cat"

def test_partial_suffix():
    assert find_longest_common_suffix(["computer", "outer", "roter"]) == "ter"

def test_empty_string_in_list():
    assert find_longest_common_suffix(["ab", "b", ""]) == ""

def test_invalid_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_invalid_input_list_with_non_strings():
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["valid", 123, "also valid"])

def test_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_common_suffix([])