import pytest
from src.character_frequency import find_most_frequent_char

def test_basic_frequency():
    assert find_most_frequent_char("hello") == 'l'
    assert find_most_frequent_char("aabbbcc") == 'b'

def test_first_frequent_character():
    assert find_most_frequent_char("abcabc") == 'a'

def test_empty_string():
    assert find_most_frequent_char("") is None

def test_single_character():
    assert find_most_frequent_char("x") == 'x'

def test_all_unique_characters():
    assert find_most_frequent_char("abcde") == 'a'

def test_invalid_input():
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)

def test_special_characters():
    assert find_most_frequent_char("!!!!hello") == '!'
    assert find_most_frequent_char("a@a@a#") == 'a'