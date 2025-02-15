import pytest
from src.most_frequent_char import find_most_frequent_character

def test_find_most_frequent_character_basic():
    assert find_most_frequent_character("hello") == "l"
    assert find_most_frequent_character("aabbcc") == "a"
    assert find_most_frequent_character("programming") == "m"

def test_find_most_frequent_character_empty_string():
    assert find_most_frequent_character("") is None

def test_find_most_frequent_character_single_character():
    assert find_most_frequent_character("x") == "x"

def test_find_most_frequent_character_first_appearance():
    # When multiple characters have the same frequency, return first appearance
    assert find_most_frequent_character("aabbcc") == "a"

def test_find_most_frequent_character_error_handling():
    with pytest.raises(TypeError):
        find_most_frequent_character(123)
    
    with pytest.raises(TypeError):
        find_most_frequent_character(None)