import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_basic_common_suffix():
    assert find_longest_common_suffix(["flower", "lower", "tower"]) == "lower"

def test_case_insensitive():
    assert find_longest_common_suffix(["HELLO", "YELLOW", "BELLOW"]) == "ello"

def test_single_string():
    assert find_longest_common_suffix(["hello"]) == "hello"

def test_no_common_suffix():
    assert find_longest_common_suffix(["cat", "dog", "bird"]) == ""

def test_empty_suffix():
    assert find_longest_common_suffix(["hello", "world"]) == ""

def test_full_match():
    assert find_longest_common_suffix(["hello", "hello", "hello"]) == "hello"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        find_longest_common_suffix("not a list")

def test_empty_list():
    with pytest.raises(ValueError):
        find_longest_common_suffix([])

def test_with_empty_string():
    assert find_longest_common_suffix(["", "hello", "world"]) == ""