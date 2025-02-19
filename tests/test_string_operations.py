import pytest
from src.string_operations import rotate_and_reverse

def test_rotate_and_reverse_basic():
    assert rotate_and_reverse("hello", 2) == "lolle"

def test_rotate_and_reverse_full_rotation():
    assert rotate_and_reverse("python", 6) == "nohtyp"

def test_rotate_and_reverse_partial_rotation():
    assert rotate_and_reverse("python", 3) == "honpyt"

def test_rotate_and_reverse_multiple_rotations():
    assert rotate_and_reverse("world", 7) == "dlrow"

def test_rotate_and_reverse_empty_string():
    assert rotate_and_reverse("", 5) == ""

def test_rotate_and_reverse_single_char():
    assert rotate_and_reverse("a", 3) == "a"

def test_rotate_and_reverse_zero_rotations():
    assert rotate_and_reverse("hello", 0) == "olleh"