import io
import sys
import pytest
from src.tower_of_hanoi import solve_tower_of_hanoi

def test_tower_of_hanoi_base_case():
    # Test with 1 disk
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    moves = solve_tower_of_hanoi(1)
    
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip()
    
    assert moves == 1
    assert output == "Move disk 1 from A to C"

def test_tower_of_hanoi_zero_disks():
    # Test with 0 disks
    moves = solve_tower_of_hanoi(0)
    assert moves == 0

def test_tower_of_hanoi_multiple_disks():
    # Test with multiple disks
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    moves = solve_tower_of_hanoi(3)
    
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip().split('\n')
    
    assert moves == 7
    assert len(output) == 7

def test_tower_of_hanoi_custom_rods():
    # Test with custom rod names
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    moves = solve_tower_of_hanoi(2, source='X', auxiliary='Y', destination='Z')
    
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip().split('\n')
    
    assert moves == 3
    assert output[0] == "Move disk 1 from X to Y"
    assert output[1] == "Move disk 2 from X to Z"
    assert output[2] == "Move disk 1 from Y to Z"

def test_tower_of_hanoi_7_disks():
    # Test total number of moves for 7 disks (should be 2^7 - 1)
    moves = solve_tower_of_hanoi(7)
    assert moves == 127  # 2^7 - 1