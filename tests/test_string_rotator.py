import pytest
from src.string_rotator import rotate_and_reverse

def test_basic_rotation_and_reverse():
    """Test basic rotation and reversal"""
    assert rotate_and_reverse("hello", 2) == "lehol"

def test_rotation_equals_length():
    """Test rotation equal to string length"""
    assert rotate_and_reverse("hello", 5) == "hello"[::-1]

def test_rotation_greater_than_length():
    """Test rotation greater than string length"""
    assert rotate_and_reverse("hello", 7) == "lehol"

def test_zero_rotations():
    """Test zero rotations"""
    assert rotate_and_reverse("hello", 0) == "olleh"

def test_empty_string():
    """Test empty string"""
    assert rotate_and_reverse("", 3) == ""

def test_invalid_input_non_string():
    """Test non-string input raises TypeError"""
    with pytest.raises(TypeError):
        rotate_and_reverse(123, 2)

def test_invalid_input_non_integer_rotations():
    """Test non-integer rotations raises TypeError"""
    with pytest.raises(TypeError):
        rotate_and_reverse("hello", "2")

def test_negative_rotations():
    """Test negative rotations raises ValueError"""
    with pytest.raises(ValueError):
        rotate_and_reverse("hello", -1)

def test_single_character_string():
    """Test rotation with single character string"""
    assert rotate_and_reverse("a", 5) == "a"