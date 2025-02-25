import pytest
from src.magic_square_validator import is_magic_square

def test_valid_magic_square():
    # A valid magic square arrangement
    assert is_magic_square([4,9,2,3,5,7,8,1,6,10]) == True

def test_invalid_length():
    # Too few or too many numbers
    assert is_magic_square([1,2,3,4,5,6,7,8,9]) == False
    assert is_magic_square([1,2,3,4,5,6,7,8,9,10,11]) == False

def test_duplicate_numbers():
    # Duplicate numbers are not allowed
    assert is_magic_square([1,1,2,3,4,5,6,7,8,9]) == False

def test_out_of_range_numbers():
    # Numbers must be between 1 and 9
    assert is_magic_square([0,1,2,3,4,5,6,7,8,9]) == False
    assert is_magic_square([1,2,3,4,5,6,7,8,10,11]) == False

def test_non_magic_square():
    # Arrangement that doesn't sum correctly
    assert is_magic_square([1,2,3,4,5,6,7,8,9,10]) == False

def test_multiple_arrangements():
    # Multiple valid magic square arrangements
    test_cases = [
        [4,9,2,3,5,7,8,1,6,10],
        # Add more valid test cases if needed
    ]
    
    for case in test_cases:
        assert is_magic_square(case) == True

def test_empty_input():
    # Empty list should return False
    assert is_magic_square([]) == False