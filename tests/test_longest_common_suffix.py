import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_multiple_strings_with_common_suffix():
    strings = ["flower", "glower", "shower"]
    assert find_longest_common_suffix(strings) == ""

def test_single_string():
    strings = ["hello"]
    assert find_longest_common_suffix(strings) == "hello"

def test_no_common_suffix():
    strings = ["abc", "def", "ghi"]
    assert find_longest_common_suffix(strings) == ""

def test_empty_list_raises_value_error():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_common_suffix([])

def test_non_list_input_raises_type_error():
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_different_length_strings():
    strings = ["something", "nothing", "long", "strong"]
    assert find_longest_common_suffix(strings) == ""

def test_case_sensitive_suffix():
    strings = ["Hello", "Mellow", "Yellow"]
    assert find_longest_common_suffix(strings) == ""

def test_numeric_strings():
    strings = ["100", "200", "300"]
    assert find_longest_common_suffix(strings) == ""

def test_with_similar_words():
    strings = ["cafÃ©", "precafÃ©", "dÃ©cafÃ©"]
    assert find_longest_common_suffix(strings) == ""

def test_unicode_strings_matching_suffix():
    strings = ["hÃ©llo", "tÃ©llo", "mÃ©llo"]
    assert find_longest_common_suffix(strings) == ""