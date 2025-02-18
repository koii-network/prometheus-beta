import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_common_prefix_multiple_strings():
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_common_prefix_single_string():
    assert find_longest_common_prefix(["hello"]) == "hello"

def test_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_common_prefix_empty_string_in_list():
    assert find_longest_common_prefix(["", "b"]) == ""

def test_common_prefix_all_empty_strings():
    assert find_longest_common_prefix(["", "", ""]) == ""

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        find_longest_common_prefix("not a list")

def test_invalid_input_empty_list():
    with pytest.raises(ValueError):
        find_longest_common_prefix([])

def test_common_prefix_case_sensitive():
    assert find_longest_common_prefix(["Hello", "hell", "help"]) == ""

def test_common_prefix_numbers_and_strings():
    assert find_longest_common_prefix(["123abc", "123def", "123ghi"]) == "123"