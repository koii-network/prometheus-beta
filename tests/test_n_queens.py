import pytest
from src.n_queens import solve_n_queens

def test_solve_n_queens_basic():
    """Test basic N-Queens solution for standard board sizes."""
    # N = 4 has 2 distinct solutions
    solutions_4 = solve_n_queens(4)
    assert len(solutions_4) == 2
    
    # Validate some known solutions for 4-queens
    expected_solutions_4 = [
        [1, 3, 0, 2],  # First known solution
        [2, 0, 3, 1]   # Second known solution
    ]
    assert solutions_4 == expected_solutions_4

def test_solve_n_queens_no_conflicts():
    """Verify that no two queens threaten each other in any solution."""
    def is_safe_solution(solution):
        n = len(solution)
        for i in range(n):
            for j in range(i+1, n):
                # Check column
                if solution[i] == solution[j]:
                    return False
                
                # Check diagonals
                if abs(solution[i] - solution[j]) == abs(i - j):
                    return False
        return True
    
    # Test for board sizes 4 to 8
    for n in range(4, 9):
        solutions = solve_n_queens(n)
        for solution in solutions:
            assert is_safe_solution(solution), f"Invalid solution for {n}-queens"

def test_solve_n_queens_board_size():
    """Test N-Queens for different board sizes."""
    # Test various board sizes
    board_sizes = [1, 4, 5, 6, 7, 8]
    expected_solutions = {
        1: 1,  # 1-queens has 1 solution
        4: 2,  # 4-queens has 2 solutions
        5: 10,  # 5-queens has 10 solutions
        6: 4,   # 6-queens has 4 solutions
        7: 40,  # 7-queens has 40 solutions
        8: 92   # 8-queens has 92 solutions
    }
    
    for n in board_sizes:
        solutions = solve_n_queens(n)
        assert len(solutions) == expected_solutions[n], f"Incorrect number of solutions for {n}-queens"

def test_solve_n_queens_empty_board():
    """Test handling of 0-queens board."""
    solutions = solve_n_queens(0)
    assert solutions == []

def test_solve_n_queens_large_board():
    """Verify that the function can handle reasonably large board sizes."""
    solutions_9 = solve_n_queens(9)
    assert len(solutions_9) > 0  # There should be multiple solutions