import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_common_suffix_multiple_strings():
    result = find_longest_common_suffix(["flower", "power", "lower"])
    assert result == "ower"

def test_single_string():
    result = find_longest_common_suffix(["hello"])
    assert result == "hello"

def test_no_common_suffix():
    result = find_longest_common_suffix(["abc", "def", "ghi"])
    assert result == ""

def test_partial_suffix():
    result = find_longest_common_suffix(["amazing", "daring", "caring"])
    assert result == "ing"

def test_empty_input_raises_error():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_common_suffix([])

def test_non_list_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_non_string_list_raises_error():
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["string", 123, "another_string"])

def test_unicode_strings():
    result = find_longest_common_suffix(["こんにちは", "ありがとう"])
    assert result == ""

def test_case_sensitive():
    result = find_longest_common_suffix(["Hello", "HELLO"])
    assert result == ""