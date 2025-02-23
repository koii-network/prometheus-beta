import pytest
from src.knights_tour import KnightsTourSolver

def test_knights_tour_solver_initialization():
    """Test the initialization of the Knights Tour Solver."""
    solver = KnightsTourSolver()
    assert solver.board_size == 8
    assert len(solver.moves) == 8

def test_valid_move_within_board():
    """Test is_valid_move method for valid moves."""
    solver = KnightsTourSolver()
    board = [[-1 for _ in range(8)] for _ in range(8)]
    assert solver.is_valid_move(3, 4, board) == True
    assert solver.is_valid_move(0, 0, board) == True

def test_valid_move_outside_board():
    """Test is_valid_move method for invalid moves."""
    solver = KnightsTourSolver()
    board = [[-1 for _ in range(8)] for _ in range(8)]
    assert solver.is_valid_move(-1, 0, board) == False
    assert solver.is_valid_move(8, 0, board) == False
    assert solver.is_valid_move(0, 8, board) == False

def test_knights_tour_solution_basic():
    """Test solving Knight's Tour from a basic starting position."""
    solver = KnightsTourSolver()
    tour = solver.solve_knights_tour(0, 0)
    
    # Check that a solution was found
    assert tour is not None
    
    # Check the first move is the starting position
    assert tour[0] == (0, 0)
    
    # Check we have exactly 64 moves (covering all squares)
    assert len(tour) == 64
    
    # Check all squares are unique
    assert len(set(tour)) == 64

def test_knights_tour_solution_different_start():
    """Test solving Knight's Tour from a different starting position."""
    solver = KnightsTourSolver()
    tour = solver.solve_knights_tour(3, 3)
    
    # Check that a solution was found
    assert tour is not None
    
    # Check the first move is the starting position
    assert tour[0] == (3, 3)
    
    # Check we have exactly 64 moves (covering all squares)
    assert len(tour) == 64
    
    # Check all squares are unique
    assert len(set(tour)) == 64