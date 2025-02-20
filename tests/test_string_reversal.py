import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_string_in_place():
    # Test normal string reversal
    s1 = list("hello")
    reverse_string_in_place(s1)
    assert s1 == list("olleh")

    # Test empty string
    s2 = list("")
    reverse_string_in_place(s2)
    assert s2 == list("")

    # Test single character string
    s3 = list("a")
    reverse_string_in_place(s3)
    assert s3 == list("a")

    # Test even-length string
    s4 = list("abcd")
    reverse_string_in_place(s4)
    assert s4 == list("dcba")

    # Test palindrome
    s5 = list("racecar")
    reverse_string_in_place(s5)
    assert s5 == list("racecar")

def test_reverse_string_type_error():
    # Test that non-list input raises a TypeError
    with pytest.raises(TypeError):
        reverse_string_in_place("not a list")