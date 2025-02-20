import pytest
from src.magic_square_validator import is_magic_square

def test_valid_magic_square():
    # A valid 3x3 magic square (with placeholder 0)
    valid_square = [0, 4, 9, 2, 3, 5, 7, 8, 1, 6]
    assert is_magic_square(valid_square) == True

def test_invalid_magic_square_wrong_length():
    # Incorrect number of elements
    invalid_square = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert is_magic_square(invalid_square) == False

def test_invalid_magic_square_duplicate_numbers():
    # Contains duplicate numbers
    invalid_square = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8]
    assert is_magic_square(invalid_square) == False

def test_invalid_magic_square_out_of_range():
    # Contains numbers outside 1-9 range
    invalid_square = [0, 1, 2, 3, 4, 5, 6, 7, 10, 9]
    assert is_magic_square(invalid_square) == False

def test_invalid_magic_square_incorrect_sum():
    # A square that doesn't meet magic square conditions
    invalid_square = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert is_magic_square(invalid_square) == False

def test_another_valid_magic_square():
    # Another valid 3x3 magic square (with placeholder 0)
    valid_square = [0, 2, 7, 6, 9, 5, 1, 4, 3, 8]
    assert is_magic_square(valid_square) == True