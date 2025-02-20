import pytest
from src.magic_square_validator import is_magic_square

def test_valid_magic_square():
    # A valid magic square where 5 is the extra/skipped number
    assert is_magic_square([8, 1, 6, 3, 5, 7, 4, 9, 2, 5]) == True

def test_valid_magic_square_different_skip():
    # Another valid magic square with a different skipped number
    assert is_magic_square([8, 1, 6, 3, 5, 7, 4, 9, 2, 8]) == True

def test_invalid_length():
    # List too short
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8]) == False
    
    # List too long
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False

def test_invalid_numbers():
    # Contains numbers outside 1-9
    assert is_magic_square([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False

def test_duplicate_numbers():
    # Contains duplicate numbers
    assert is_magic_square([1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False

def test_not_a_magic_square():
    # Numbers that do not form a magic square
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 5]) == False