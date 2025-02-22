import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_case():
    assert find_most_frequent_char("hello") == 'l'
    assert find_most_frequent_char("aabbcccc") == 'c'

def test_first_repeated_char():
    assert find_most_frequent_char("aabbccddee") == 'a'

def test_single_char():
    assert find_most_frequent_char("a") == 'a'

def test_mixed_case():
    assert find_most_frequent_char("hElLo") == 'l'  # Case-sensitive

def test_with_spaces_and_special_chars():
    assert find_most_frequent_char("hello world!!") == 'l'

def test_empty_string_raises_error():
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_char("")