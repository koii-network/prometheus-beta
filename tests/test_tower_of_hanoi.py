import pytest
from src.tower_of_hanoi import tower_of_hanoi

def test_tower_of_hanoi_base_case():
    """Test the base case with 1 disk"""
    moves = tower_of_hanoi(1, 'A', 'C', 'B')
    assert len(moves) == 1
    assert moves[0] == "Move disk 1 from A to C"

def test_tower_of_hanoi_2_disks():
    """Test the case with 2 disks"""
    moves = tower_of_hanoi(2, 'A', 'C', 'B')
    assert len(moves) == 3
    assert moves == [
        "Move disk 1 from A to B",
        "Move disk 2 from A to C",
        "Move disk 1 from B to C"
    ]

def test_tower_of_hanoi_7_disks():
    """Test the case with 7 disks"""
    moves = tower_of_hanoi(7, 'A', 'C', 'B')
    assert len(moves) == 127  # 2^7 - 1 moves for 7 disks

def test_tower_of_hanoi_invalid_input():
    """Test the case with invalid input"""
    moves = tower_of_hanoi(0)
    assert len(moves) == 0

def test_tower_of_hanoi_custom_rods():
    """Test with custom rod names"""
    moves = tower_of_hanoi(3, 'X', 'Z', 'Y')
    assert len(moves) == 7
    assert "Move disk from X to" in moves[0]
    assert "Move disk from Y to Z" in moves[-1]