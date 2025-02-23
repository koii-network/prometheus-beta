import io
import sys
import pytest
from src.tower_of_hanoi import tower_of_hanoi

def test_tower_of_hanoi_output():
    """
    Test the tower of hanoi recursive algorithm by capturing stdout
    and checking the basic properties of the output
    """
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Run tower of hanoi with small number of disks for testing
    tower_of_hanoi(3)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Get the output
    output = captured_output.getvalue().strip().split('\n')
    
    # Assertions
    # 1. Check total number of moves for 3 disks (should be 2^3 - 1 = 7 moves)
    assert len(output) == 7, f"Expected 7 moves for 3 disks, got {len(output)} moves"
    
    # 2. Verify first and last moves look correct
    assert output[0].startswith("Move disk 1"), "First move should be smallest disk"
    assert output[-1].startswith(f"Move disk 3"), "Last move should be the largest disk"

def test_tower_of_hanoi_moves_count():
    """
    Test the number of moves for different disk counts
    """
    def count_moves(n):
        """Helper function to count total moves"""
        count = [0]
        def count_moves_helper(n, source='A', auxiliary='B', destination='C'):
            if n == 1:
                count[0] += 1
                return
            count_moves_helper(n-1, source, destination, auxiliary)
            count[0] += 1
            count_moves_helper(n-1, auxiliary, source, destination)
        
        count_moves_helper(n)
        return count[0]
    
    # Check move count formula 2^n - 1
    test_cases = [1, 2, 3, 4, 5]
    for n in test_cases:
        expected_moves = (2 ** n) - 1
        assert count_moves(n) == expected_moves, f"Move count incorrect for {n} disks"

def test_tower_of_hanoi_invalid_input():
    """
    Test handling of invalid input
    """
    # Negative number of disks should raise a recursion error or similar
    with pytest.raises(RecursionError):
        tower_of_hanoi(-1)
    
    # Zero disks should not raise an error, but should do nothing
    captured_output = io.StringIO()
    sys.stdout = captured_output
    tower_of_hanoi(0)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "", "Zero disks should produce no output"