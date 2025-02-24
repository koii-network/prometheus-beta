import pytest
from src.n_queens import solve_n_queens

def test_solve_n_queens_invalid_input():
    """Test that invalid input raises a ValueError"""
    with pytest.raises(ValueError):
        solve_n_queens(0)
    with pytest.raises(ValueError):
        solve_n_queens(-1)

def test_solve_n_queens_1x1():
    """Test 1x1 board solution"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert solutions[0] == [0]

def test_solve_n_queens_4x4():
    """Test 4x4 board solution"""
    solutions = solve_n_queens(4)
    
    # Expected solutions for 4x4 board
    expected_solutions = [
        [1, 3, 0, 2],
        [2, 0, 3, 1]
    ]
    
    # Check number of solutions
    assert len(solutions) == 2
    
    # Verify solutions
    for solution in solutions:
        assert solution in expected_solutions
        assert len(solution) == 4

def test_solution_validity():
    """Thoroughly validate N-Queens solutions for a few board sizes"""
    for n in range(1, 6):  # Test board sizes 1 to 5
        solutions = solve_n_queens(n)
        
        # Check each solution
        for solution in solutions:
            # Check solution length matches board size
            assert len(solution) == n
            
            # Validate no two queens in same row or column by construction
            assert len(set(solution)) == n
            
            # Check diagonals
            for i in range(n):
                for j in range(i+1, n):
                    # Check diagonals
                    assert abs(solution[i] - solution[j]) != abs(i - j)

def test_solutions_unique():
    """Ensure solutions are unique"""
    n = 4
    solutions = solve_n_queens(n)
    assert len(solutions) == len(set(tuple(sol) for sol in solutions))

def test_large_board_solvable():
    """Test a slightly larger board is solvable"""
    n = 6
    solutions = solve_n_queens(n)
    assert len(solutions) > 0  # Ensure solutions exist
    
    # Basic validation of solutions
    for solution in solutions:
        assert len(solution) == n
        assert len(set(solution)) == n  # No repeated columns