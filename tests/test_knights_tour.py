import pytest
from src.knights_tour import KnightsTourSolver

def test_knights_tour_existence():
    """Test that the KnightsTourSolver class exists"""
    solver = KnightsTourSolver()
    assert solver is not None

def test_knights_tour_valid_tour():
    """Test that a valid knights tour is found"""
    solver = KnightsTourSolver()
    tour = solver.solve_knights_tour(0, 0)
    
    # Check that a tour exists
    assert tour is not None
    
    # Check tour length is correct (64 moves for 8x8 board)
    assert len(tour) == 64
    
    # Check all moves are unique
    assert len(set(tour)) == 64

def test_knights_tour_move_validity():
    """Test that moves are valid knight moves"""
    solver = KnightsTourSolver()
    tour = solver.solve_knights_tour(0, 0)
    
    # Check each consecutive move is a valid knight's move
    for i in range(len(tour) - 1):
        x1, y1 = tour[i]
        x2, y2 = tour[i+1]
        
        # Calculate move differences
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        # Verify it's a valid knight's move
        assert (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

def test_knights_tour_board_boundaries():
    """Test tour stays within board boundaries"""
    solver = KnightsTourSolver()
    tour = solver.solve_knights_tour(0, 0)
    
    # Check all moves are within 8x8 board
    for x, y in tour:
        assert 0 <= x < 8
        assert 0 <= y < 8

def test_knights_tour_different_start_positions():
    """Test tours can be found from different start positions"""
    solver = KnightsTourSolver()
    
    # Test multiple start positions
    start_positions = [(0, 0), (3, 3), (7, 7), (2, 5)]
    
    for start_x, start_y in start_positions:
        tour = solver.solve_knights_tour(start_x, start_y)
        
        # Check a valid tour is found
        assert tour is not None
        assert len(tour) == 64
        assert tour[0] == (start_x, start_y)  # Tour starts at specified position