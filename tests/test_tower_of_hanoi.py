import io
import sys
import pytest
from src.tower_of_hanoi import tower_of_hanoi, solve_tower_of_hanoi

def test_tower_of_hanoi_single_disk(capsys):
    tower_of_hanoi(1, 'A', 'B', 'C')
    captured = capsys.readouterr()
    assert captured.out.strip() == "Move disk 1 from A to C"

def test_tower_of_hanoi_three_disks(capsys):
    tower_of_hanoi(3, 'A', 'B', 'C')
    captured = capsys.readouterr()
    moves = captured.out.strip().split('\n')
    
    # Verify number of moves
    assert len(moves) == 7  # 2^3 - 1 moves for 3 disks
    
    # Some basic move validations
    assert "Move disk 1 from A to C" in moves
    assert "Move disk 2 from A to B" in moves
    assert "Move disk 3 from A to C" in moves

def test_solve_tower_of_hanoi_output(capsys):
    solve_tower_of_hanoi()
    captured = capsys.readouterr()
    moves = captured.out.strip().split('\n')
    
    # Verify number of moves
    assert len(moves) == 127  # 2^7 - 1 moves for 7 disks
    
    # Basic move validations
    assert moves[0].startswith("Move disk 1")
    assert len(moves) == 127  # 2^7 - 1 moves for 7 disks

def test_tower_of_hanoi_validate_rod_names():
    # Test various valid rod name combinations
    tower_of_hanoi(2, 'Source', 'Mid', 'Dest')
    tower_of_hanoi(3, 'Left', 'Center', 'Right')
    
    # Ensure different rod names are used
    with pytest.raises(ValueError):
        tower_of_hanoi(2, 'A', 'A', 'B')
    with pytest.raises(ValueError):
        tower_of_hanoi(2, 'A', 'B', 'A')