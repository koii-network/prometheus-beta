import pytest
from src.n_queens import solve_n_queens

def test_solve_n_queens_basic_cases():
    # Test for 1x1 board (trivial case)
    assert len(solve_n_queens(1)) == 1
    
    # Test for 4x4 board
    solutions_4 = solve_n_queens(4)
    assert len(solutions_4) == 2
    
    # Test for 8x8 board
    solutions_8 = solve_n_queens(8)
    assert len(solutions_8) == 92

def test_n_queens_solution_validation():
    def validate_solution(n, solution):
        # Ensure solution has correct number of queens
        assert len(solution) == n
        
        # Check no two queens share same row or column
        rows = set()
        cols = set()
        for row, col in solution:
            assert 0 <= row < n
            assert 0 <= col < n
            assert row not in rows
            assert col not in cols
            rows.add(row)
            cols.add(col)
        
        # Check diagonals
        for i in range(len(solution)):
            for j in range(i+1, len(solution)):
                r1, c1 = solution[i]
                r2, c2 = solution[j]
                assert abs(r1 - r2) != abs(c1 - c2)
    
    # Validate solutions for different board sizes
    for n in range(1, 5):
        solutions = solve_n_queens(n)
        for solution in solutions:
            validate_solution(n, solution)

def test_edge_cases():
    # Test very small board
    assert len(solve_n_queens(0)) == 0
    
    # Test for small board sizes where no solutions exist
    assert len(solve_n_queens(2)) == 0
    assert len(solve_n_queens(3)) == 0

def test_solution_count():
    # Predefined expected solution counts for different board sizes
    expected_counts = {
        1: 1,   # 1x1 board
        4: 2,   # 4x4 board
        8: 92   # 8x8 board
    }
    
    for n, expected_count in expected_counts.items():
        solutions = solve_n_queens(n)
        assert len(solutions) == expected_count