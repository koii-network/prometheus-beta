import pytest
from src.prime_path_finder import find_prime_number_path, is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False

def test_prime_path_simple_grid():
    grid = [
        [2, 3, 5],
        [7, 11, 13],
        [17, 19, 23]
    ]
    path = find_prime_number_path(grid)
    assert path is not None
    # Verify path forms a prime number
    assert is_prime(int(''.join(map(str, [grid[x][y] for x, y in path]))))

def test_prime_path_no_solution():
    grid = [
        [4, 6, 8],
        [10, 12, 14],
        [16, 18, 20]
    ]
    path = find_prime_number_path(grid)
    assert path is None

def test_prime_path_complex_grid():
    grid = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29, 31, 37]
    ]
    path = find_prime_number_path(grid)
    assert path is not None
    # Verify path forms a prime number
    assert is_prime(int(''.join(map(str, [grid[x][y] for x, y in path]))))

def test_empty_grid():
    grid = []
    path = find_prime_number_path(grid)
    assert path is None

def test_single_cell_grid():
    grid = [[2]]  # A prime number
    path = find_prime_number_path(grid)
    assert path == [(0, 0)]

def test_tricky_grid_with_multiple_primes():
    grid = [
        [2, 3, 5],
        [23, 7, 11],
        [29, 31, 37]
    ]
    path = find_prime_number_path(grid)
    assert path is not None
    # Verify path forms a prime number
    assert is_prime(int(''.join(map(str, [grid[x][y] for x, y in path]))))