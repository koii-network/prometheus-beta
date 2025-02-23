import pytest
from src.string_reverser import reverse_string_with_rules

def test_empty_string():
    assert reverse_string_with_rules("") == ""

def test_simple_word_reversal():
    assert reverse_string_with_rules("hello") == "olleh"
    assert reverse_string_with_rules("world") == "dlrow"

def test_multiple_words():
    assert reverse_string_with_rules("hello world") == "olleh dlrow"

def test_palindromes():
    assert reverse_string_with_rules("radar") == "radar"
    assert reverse_string_with_rules("hello radar world") == "olleh radar dlrow"

def test_numbers():
    assert reverse_string_with_rules("123") == "321"
    assert reverse_string_with_rules("hello 123 world") == "olleh 321 dlrow"

def test_mixed_tokens():
    assert reverse_string_with_rules("hello 123 radar world") == "olleh 321 radar dlrow"
    assert reverse_string_with_rules("a1b2c3d") == "a1b2c3d"

def test_punctuation():
    assert reverse_string_with_rules("hello, world!") == "olleh, dlrow!"
    assert reverse_string_with_rules("123, abc, radar") == "321, cba, radar"

def test_invalid_input():
    with pytest.raises(TypeError):
        reverse_string_with_rules(None)
    with pytest.raises(TypeError):
        reverse_string_with_rules(123)

def test_complex_scenarios():
    assert reverse_string_with_rules("12radar34") == "12radar43"
    assert reverse_string_with_rules("hello123world") == "olleh321dlrow"