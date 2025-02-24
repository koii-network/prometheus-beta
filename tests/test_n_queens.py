import pytest
from src.n_queens import solve_n_queens, count_n_queens_solutions

def test_solve_n_queens_1x1():
    """Test 1x1 board solution"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert solutions[0] == [0]

def test_solve_n_queens_4x4():
    """Test 4x4 board solutions"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2
    
    # Check that solutions are valid
    for solution in solutions:
        assert len(solution) == 4
        assert len(set(solution)) == 4  # No repeated columns
        _validate_solution(solution, 4)

def test_solve_n_queens_8x8():
    """Test 8x8 board solution count"""
    solution_count = count_n_queens_solutions(8)
    assert solution_count == 92

def test_n_queens_invalid_input():
    """Test invalid input handling"""
    with pytest.raises(ValueError):
        solve_n_queens(0)
    
    with pytest.raises(ValueError):
        solve_n_queens(-1)
    
    with pytest.raises(ValueError):
        solve_n_queens("not an integer")

def _validate_solution(solution, n):
    """
    Validate a single N-Queens solution.
    
    Args:
        solution (list): Solution representing column positions of queens.
        n (int): Board size.
    """
    # Check no two queens in same column (already ensured by solution construction)
    assert len(set(solution)) == n
    
    # Check diagonals
    for i in range(n):
        for j in range(i + 1, n):
            # Check diagonal conflict
            assert abs(solution[i] - solution[j]) != abs(i - j), \
                f"Queens in rows {i} and {j} are on a diagonal"