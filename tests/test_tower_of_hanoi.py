import pytest
from src.tower_of_hanoi import tower_of_hanoi

def test_tower_of_hanoi_basic():
    """Test basic functionality with 1 disk"""
    moves = tower_of_hanoi(1)
    assert len(moves) == 1
    assert moves[0] == ('A', 'C')

def test_tower_of_hanoi_3_disks():
    """Test scenario with 3 disks"""
    moves = tower_of_hanoi(3)
    assert len(moves) == 7  # 2^3 - 1 moves
    
def test_tower_of_hanoi_7_disks():
    """Test scenario with 7 disks"""
    moves = tower_of_hanoi(7)
    assert len(moves) == 127  # 2^7 - 1 moves
    
def test_tower_of_hanoi_custom_rods():
    """Test with custom rod names"""
    moves = tower_of_hanoi(2, 'Source', 'Temp', 'Destination')
    assert len(moves) == 3
    assert moves[0] == ('Source', 'Temp')
    assert moves[1] == ('Source', 'Destination')
    assert moves[2] == ('Temp', 'Destination')

def test_tower_of_hanoi_zero_disks():
    """Test with zero disks"""
    moves = tower_of_hanoi(0)
    assert len(moves) == 0

def test_move_count_formula():
    """Verify that the number of moves follows 2^n - 1 formula"""
    test_cases = [1, 2, 3, 4, 5, 6, 7]
    for n in test_cases:
        moves = tower_of_hanoi(n)
        assert len(moves) == (2**n - 1), f"Failed for {n} disks"