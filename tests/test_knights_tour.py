import pytest
from src.knights_tour import solve_knights_tour

def test_knights_tour_solver():
    """Test the Knight's Tour solver with various start positions"""
    # Test different starting positions
    start_positions = [
        (0, 0),   # Top-left corner
        (7, 7),   # Bottom-right corner
        (3, 3),   # Middle of the board
        (2, 1),   # Random intermediate position
    ]
    
    for start_x, start_y in start_positions:
        tour = solve_knights_tour(start_x, start_y)
        
        # Check that a tour was found
        assert tour is not None, f"No tour found for start position ({start_x}, {start_y})"
        
        # Check tour properties
        assert len(tour) == 64, f"Tour should have 64 squares for ({start_x}, {start_y})"
        
        # Check that all squares are unique
        assert len(set(tour)) == 64, f"Tour should have unique squares for ({start_x}, {start_y})"
        
        # Check that tour starts at the correct position
        assert tour[0] == (start_x, start_y), f"Tour must start at ({start_x}, {start_y})"
        
        # Validate each move is a valid knight's move
        knight_moves = {
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        }
        
        for i in range(len(tour) - 1):
            x1, y1 = tour[i]
            x2, y2 = tour[i+1]
            move = (x2 - x1, y2 - y1)
            assert move in knight_moves, f"Invalid knight move from {tour[i]} to {tour[i+1]}"

def test_invalid_start_positions():
    """Test start positions that are out of board bounds"""
    invalid_positions = [
        (-1, 0),  # Negative x
        (0, -1),  # Negative y
        (8, 0),   # x out of bounds
        (0, 8),   # y out of bounds
    ]
    
    for start_x, start_y in invalid_positions:
        with pytest.raises(IndexError):
            solve_knights_tour(start_x, start_y)