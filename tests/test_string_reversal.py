import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_string_in_place():
    # Test normal string reversal
    s1 = list("hello")
    reverse_string_in_place(s1)
    assert s1 == list("olleh")

def test_reverse_empty_string():
    # Test empty string
    s2 = []
    reverse_string_in_place(s2)
    assert s2 == []

def test_reverse_single_character():
    # Test single character
    s3 = list("a")
    reverse_string_in_place(s3)
    assert s3 == list("a")

def test_reverse_even_length_string():
    # Test even length string
    s4 = list("abcd")
    reverse_string_in_place(s4)
    assert s4 == list("dcba")

def test_reverse_odd_length_string():
    # Test odd length string
    s5 = list("python")
    reverse_string_in_place(s5)
    assert s5 == list("nohtyp")

def test_reverse_with_special_characters():
    # Test string with special characters
    s6 = list("a1b2c3")
    reverse_string_in_place(s6)
    assert s6 == list("3c2b1a")

def test_immutability():
    # Ensure the function works in-place
    s7 = list("testing")
    original_id = id(s7)
    reverse_string_in_place(s7)
    assert id(s7) == original_id  # Same object
    assert s7 == list("gnitset")  # Correctly reversed