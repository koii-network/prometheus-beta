import pytest
from src.prime_path_finder import find_prime_sequence_path, is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False

def test_find_prime_sequence_path_basic():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = find_prime_sequence_path(grid)
    assert len(result) > 0, "Should find a prime sequence path"
    assert all(0 <= r < 3 and 0 <= c < 3 for r, c in result), "Path should be within grid"

def test_find_prime_sequence_path_complex():
    grid = [
        [2, 3, 5],
        [7, 11, 13],
        [17, 19, 23]
    ]
    result = find_prime_sequence_path(grid)
    assert len(result) > 1, "Should find a multi-cell prime sequence path"
    
    # Verify sequence forms a prime when concatenated
    sequence = [grid[r][c] for r, c in result]
    sequence_num = int(''.join(map(str, sequence)))
    assert is_prime(sequence_num), "Concatenated sequence should be prime"

def test_find_prime_sequence_path_empty_grid():
    grid = []
    result = find_prime_sequence_path(grid)
    assert result == [], "Empty grid should return empty path"

def test_find_prime_sequence_path_no_prime_sequence():
    grid = [
        [4, 6, 8],
        [10, 12, 14],
        [16, 18, 20]
    ]
    result = find_prime_sequence_path(grid)
    assert result == [], "Grid with no prime sequences should return empty path"