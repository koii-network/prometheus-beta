import pytest
from src.most_frequent_char import find_most_frequent_character

def test_most_frequent_character_basic():
    assert find_most_frequent_character('aabbccde') == 'a'
    assert find_most_frequent_character('hello') == 'l'
    assert find_most_frequent_character('programming') == 'r'

def test_most_frequent_character_single_char():
    assert find_most_frequent_character('z') == 'z'

def test_most_frequent_character_empty_string():
    assert find_most_frequent_character('') is None

def test_most_frequent_character_equal_frequency():
    # When multiple characters have the same frequency, return the first one
    assert find_most_frequent_character('aabb') == 'a'
    assert find_most_frequent_character('1122') == '1'

def test_most_frequent_character_with_spaces_and_special_chars():
    assert find_most_frequent_character('hello world!') == 'l'
    assert find_most_frequent_character('!!!!!') == '!'