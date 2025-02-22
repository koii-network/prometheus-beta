import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicates_basic():
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbccdd") == "abcd"
    assert remove_duplicate_chars("") == ""

def test_remove_duplicates_preserve_order():
    assert remove_duplicate_chars("abracadabra") == "abracd"
    assert remove_duplicate_chars("mississippi") == "misp"

def test_remove_duplicates_with_spaces_and_punctuation():
    assert remove_duplicate_chars("  hello  world  ") == " helo wrd"
    assert remove_duplicate_chars("a.b.c.a.b.c") == "a.bc"

def test_remove_duplicates_error_handling():
    with pytest.raises(TypeError):
        remove_duplicate_chars(12345)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
    with pytest.raises(TypeError):
        remove_duplicate_chars(["hello"])