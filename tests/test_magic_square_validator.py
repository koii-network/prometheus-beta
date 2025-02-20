import pytest
from src.magic_square_validator import is_magic_square

def test_valid_magic_square():
    # A valid 3x3 magic square (with 0 as placeholder)
    valid_square = [0, 2, 7, 6, 9, 5, 1, 4, 3, 8]
    assert is_magic_square(valid_square) == True

def test_invalid_magic_square_wrong_rows():
    # A square with incorrect row sums
    invalid_square = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert is_magic_square(invalid_square) == False

def test_invalid_magic_square_duplicate_numbers():
    # A square with duplicate numbers
    duplicate_square = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert is_magic_square(duplicate_square) == False

def test_invalid_magic_square_out_of_range():
    # A square with numbers out of 1-9 range
    out_of_range_square = [0, 1, 2, 3, 10, 5, 6, 7, 8, 9]
    assert is_magic_square(out_of_range_square) == False

def test_invalid_input_length():
    # List too short
    short_list = [0, 1, 2, 3]
    assert is_magic_square(short_list) == False

    # List too long
    long_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert is_magic_square(long_list) == False

def test_non_list_input():
    # Non-list inputs
    assert is_magic_square(None) == False
    assert is_magic_square("not a list") == False
    assert is_magic_square(123) == False