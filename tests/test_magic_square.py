import pytest
from src.magic_square import is_magic_square

def test_valid_magic_square():
    """Test a valid 3x3 magic square."""
    # A classic magic square with numbers 1-9
    assert is_magic_square([8, 1, 6, 3, 5, 7, 4, 9, 2, 0]) == True

def test_invalid_length():
    """Test input with incorrect number of elements."""
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False

def test_non_unique_numbers():
    """Test input with duplicate numbers."""
    assert is_magic_square([1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == False

def test_out_of_range_numbers():
    """Test input with numbers outside 1-9 range."""
    assert is_magic_square([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert is_magic_square([10, 11, 12, 13, 14, 15, 16, 17, 18, 0]) == False

def test_non_magic_square():
    """Test a non-magic square arrangement."""
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == False

def test_invalid_input_type():
    """Test non-list input."""
    assert is_magic_square("not a list") == False
    assert is_magic_square(123) == False
    assert is_magic_square(None) == False

def test_magic_square_with_zeros():
    """Test a magic square with an additional zero at the end."""
    # Arrange the magic square with a zero as the last element
    assert is_magic_square([8, 1, 6, 3, 5, 7, 4, 9, 2, 0]) == True