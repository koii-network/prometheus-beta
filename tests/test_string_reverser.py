import pytest
from src.string_reverser import reverse_string_with_rules

def test_empty_string():
    assert reverse_string_with_rules("") == ""

def test_simple_string():
    assert reverse_string_with_rules("hello") == "olleh"

def test_string_with_numbers():
    assert reverse_string_with_rules("hello123world") == "olleh321dlrow"

def test_palindrome_preservation():
    assert reverse_string_with_rules("racecar and bob") == "racecar dna bob"

def test_mixed_complexity():
    assert reverse_string_with_rules("12abc321 bob racecar") == "21cba123 bob racecar"

def test_special_characters():
    assert reverse_string_with_rules("hello, world! 123") == "olleh, dlrow! 321"

def test_edge_cases():
    assert reverse_string_with_rules("a") == "a"
    assert reverse_string_with_rules("1") == "1"

def test_invalid_input():
    with pytest.raises(TypeError):
        reverse_string_with_rules(None)
    with pytest.raises(TypeError):
        reverse_string_with_rules(123)