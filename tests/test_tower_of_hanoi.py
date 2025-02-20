import pytest
from src.tower_of_hanoi import solve_tower_of_hanoi

def test_tower_of_hanoi_zero_disks():
    """Test Tower of Hanoi with zero disks"""
    moves = solve_tower_of_hanoi(0)
    assert len(moves) == 0

def test_tower_of_hanoi_one_disk():
    """Test Tower of Hanoi with one disk"""
    moves = solve_tower_of_hanoi(1)
    assert len(moves) == 1
    assert moves[0] == ('A', 'C')

def test_tower_of_hanoi_three_disks():
    """Test Tower of Hanoi with three disks"""
    moves = solve_tower_of_hanoi(3)
    assert len(moves) == 7  # 2^n - 1 total moves

def test_tower_of_hanoi_custom_rod_names():
    """Test Tower of Hanoi with custom rod names"""
    moves = solve_tower_of_hanoi(2, source_rod='X', auxiliary_rod='Y', destination_rod='Z')
    assert moves[0] == ('X', 'Y')
    assert moves[1] == ('X', 'Z')
    assert moves[2] == ('Y', 'Z')

def test_tower_of_hanoi_invalid_input():
    """Test Tower of Hanoi with invalid input"""
    with pytest.raises(ValueError):
        solve_tower_of_hanoi(-1)
    
    with pytest.raises(ValueError):
        solve_tower_of_hanoi('invalid')

def test_tower_of_hanoi_seven_disks():
    """Test Tower of Hanoi with seven disks"""
    moves = solve_tower_of_hanoi(7)
    assert len(moves) == 127  # 2^n - 1 total moves