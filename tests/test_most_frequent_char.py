import pytest
from src.most_frequent_char import find_most_frequent_char

def test_most_frequent_char_normal_case():
    assert find_most_frequent_char("hello") == 'l'
    assert find_most_frequent_char("programming") == 'r'
    assert find_most_frequent_char("aabbccc") == 'c'

def test_most_frequent_char_first_in_case_of_tie():
    assert find_most_frequent_char("aabbcc") == 'a'
    assert find_most_frequent_char("abbccc") == 'b'

def test_most_frequent_char_empty_string():
    assert find_most_frequent_char("") is None

def test_most_frequent_char_single_char():
    assert find_most_frequent_char("a") == 'a'

def test_most_frequent_char_with_spaces():
    assert find_most_frequent_char("hello world") == 'l'

def test_most_frequent_char_error_cases():
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)
    with pytest.raises(TypeError):
        find_most_frequent_char(["hello"])