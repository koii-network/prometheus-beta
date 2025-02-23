import pytest
from src.prime_path_finder import find_prime_path, is_prime

def test_is_prime():
    # Test prime number detection
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(4) == False
    assert is_prime(15) == False

def test_find_prime_path_basic():
    # Simple grid with a prime path
    grid = [
        [2, 3, 5],
        [7, 11, 13],
        [17, 19, 23]
    ]
    path = find_prime_path(grid)
    assert len(path) > 0, "Should find a prime path"
    assert all(is_prime(grid[r][c]) for r, c in path), "All path elements should be prime"

def test_find_prime_path_no_path():
    # Grid with no prime path
    grid = [
        [4, 6, 8],
        [10, 12, 14],
        [16, 18, 20]
    ]
    path = find_prime_path(grid)
    assert len(path) == 0, "Should return empty path when no prime sequence exists"

def test_find_prime_path_complex():
    # More complex grid with prime path
    grid = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29, 31, 37]
    ]
    path = find_prime_path(grid)
    assert len(path) > 0, "Should find a valid prime path"
    
    # Verify the path contains only adjacent prime numbers
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i+1]
        assert abs(r1 - r2) + abs(c1 - c2) == 1, "Path should be continuous"
        assert is_prime(grid[r1][c1] + grid[r2][c2]), "Adjacent primes should form a prime"

def test_empty_grid():
    # Test with empty grid
    grid = []
    path = find_prime_path(grid)
    assert len(path) == 0, "Should handle empty grid"

def test_single_cell_grid():
    # Test with single cell grid
    grid = [[2]]  # Prime number
    path = find_prime_path(grid)
    assert len(path) == 1, "Should work with single prime cell"
    assert path[0] == (0, 0), "Should return the single cell"

def test_single_cell_non_prime_grid():
    # Test with single non-prime cell
    grid = [[4]]  # Non-prime number
    path = find_prime_path(grid)
    assert len(path) == 0, "Should return empty path for non-prime single cell"