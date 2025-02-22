import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_common_prefix_multiple_strings():
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_common_prefix_single_string():
    assert find_longest_common_prefix(["hello"]) == "hello"

def test_common_prefix_empty_list():
    assert find_longest_common_prefix([]) == ""

def test_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_common_prefix_case_sensitive():
    assert find_longest_common_prefix(["Hello", "hello"]) == ""

def test_common_prefix_different_lengths():
    assert find_longest_common_prefix(["abc", "abcd", "ab"]) == "ab"

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        find_longest_common_prefix("not a list")

def test_invalid_input_non_string_elements():
    with pytest.raises(TypeError):
        find_longest_common_prefix(["string", 123, "another_string"])

def test_common_prefix_unicode():
    assert find_longest_common_prefix(["café", "cafés", "café-au-lait"]) == "café"