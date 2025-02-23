import pytest
from src.n_queens_solver import solve_n_queens

def validate_solution(n, solution):
    """
    Validate a single solution for the N-Queens problem.
    
    Args:
        n (int): Size of the board
        solution (list): A solution representing queen positions
    
    Returns:
        bool: True if solution is valid, False otherwise
    """
    # Check length of solution
    assert len(solution) == n, f"Solution length should be {n}"
    
    # Check unique column placements
    assert len(set(solution)) == n, "Queens must be in unique columns"
    
    # Check diagonals
    for i in range(n):
        for j in range(i+1, n):
            # Check diagonal threats
            assert abs(solution[i] - solution[j]) != abs(i - j), \
                f"Queens at rows {i} and {j} threaten each other diagonally"

def test_n_queens_solver_base_cases():
    """Test N-Queens solver for small board sizes."""
    test_cases = [
        (1, 1),   # 1x1 board
        (4, 2),   # Classic 4-queens problem
        (8, 92)   # Standard 8-queens problem
    ]
    
    for board_size, expected_solutions in test_cases:
        solutions = solve_n_queens(board_size)
        
        # Validate number of solutions
        assert len(solutions) == expected_solutions, \
            f"Incorrect number of solutions for {board_size}-queens"
        
        # Validate each solution
        for solution in solutions:
            validate_solution(board_size, solution)

def test_n_queens_solver_edge_cases():
    """Test edge cases and unusual board sizes."""
    test_cases = [
        (2, 0),   # No solutions possible
        (3, 0),   # No solutions possible
        (5, 10)   # 5-queens problem
    ]
    
    for board_size, expected_solutions in test_cases:
        solutions = solve_n_queens(board_size)
        
        # Validate number of solutions
        assert len(solutions) == expected_solutions, \
            f"Incorrect number of solutions for {board_size}-queens"
        
        # Validate each solution
        for solution in solutions:
            validate_solution(board_size, solution)

def test_n_queens_solver_input_validation():
    """Test input validation and boundary conditions."""
    invalid_cases = [0, -1, -10]
    
    for invalid_size in invalid_cases:
        with pytest.raises(Exception):
            solve_n_queens(invalid_size)