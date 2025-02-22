import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_string():
    assert find_most_frequent_char("hello") == "l"

def test_all_unique_chars():
    assert find_most_frequent_char("abcde") == "a"  # Returns first character if all are unique

def test_multiple_max_frequency_chars():
    result = find_most_frequent_char("aabbcc")
    assert result in ["a", "b", "c"]  # Any of these are valid

def test_string_with_spaces():
    assert find_most_frequent_char("hello world") == " "

def test_string_with_special_chars():
    assert find_most_frequent_char("hello!!") == "!"

def test_empty_string_raises_error():
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_char("")

def test_single_char_string():
    assert find_most_frequent_char("x") == "x"

def test_case_sensitivity():
    assert find_most_frequent_char("Hello") == "l"  # Lowercase 'l'