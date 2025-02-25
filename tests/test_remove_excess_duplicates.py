import pytest
from src.remove_excess_duplicates import remove_excess_duplicates

def test_remove_excess_duplicates_basic():
    assert remove_excess_duplicates("aabbcccd") == "aabbcd"
    assert remove_excess_duplicates("hello") == "helo"
    assert remove_excess_duplicates("aaaaabbbcccccd") == "aabbbcd"

def test_remove_excess_duplicates_empty_string():
    assert remove_excess_duplicates("") == ""

def test_remove_excess_duplicates_no_duplicates():
    assert remove_excess_duplicates("abcdef") == "abcdef"

def test_remove_excess_duplicates_all_same_chars():
    assert remove_excess_duplicates("aaaaaaa") == "aa"

def test_remove_excess_duplicates_error_handling():
    with pytest.raises(TypeError):
        remove_excess_duplicates(123)
    with pytest.raises(TypeError):
        remove_excess_duplicates(None)

def test_remove_excess_duplicates_mixed_case():
    assert remove_excess_duplicates("AaAaAaABBBccc") == "AaAaABBccc"