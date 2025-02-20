import pytest
from src.ball_stack_sorter import BallStackSorter

def test_initialization_valid():
    """Test valid initialization of BallStackSorter"""
    stacks = {
        'Red': ['R1', 'R2', 'R3'],
        'Blue': ['B1', 'B2', 'B3'],
        'Green': ['G1', 'G2', 'G3']
    }
    sorter = BallStackSorter(stacks)
    assert sorter.total_balls == 9
    assert sorter.target_stack_size == 3

def test_initialization_invalid():
    """Test invalid initialization with uneven ball distribution"""
    stacks = {
        'Red': ['R1', 'R2'],
        'Blue': ['B1', 'B2', 'B3'],
        'Green': ['G1', 'G2', 'G3']
    }
    with pytest.raises(ValueError, match="Total number of balls must be divisible equally among stacks"):
        BallStackSorter(stacks)

def test_can_move():
    """Test the can_move method"""
    stacks = {
        'Red': ['R1', 'R2', 'R3'],
        'Blue': ['B1', 'B2'],
        'Green': ['G1']
    }
    sorter = BallStackSorter(stacks)
    
    # Can move from Red to Blue
    assert sorter.can_move('Red', 'Blue') is True
    
    # Can move from Red to Green
    assert sorter.can_move('Red', 'Green') is True
    
    # Cannot move to a full stack
    stacks_full = {
        'Red': ['R1', 'R2', 'R3'],
        'Blue': ['B1', 'B2', 'B3'],
        'Green': ['G1', 'G2', 'G3']
    }
    full_sorter = BallStackSorter(stacks_full)
    assert full_sorter.can_move('Red', 'Blue') is False

def test_move_ball():
    """Test moving a ball between stacks"""
    stacks = {
        'Red': ['R1', 'R2', 'R3'],
        'Blue': ['B1', 'B2'],
        'Green': ['G1']
    }
    sorter = BallStackSorter(stacks)
    
    sorter.move_ball('Red', 'Blue')
    assert sorter.stacks['Red'] == ['R1', 'R2']
    assert sorter.stacks['Blue'] == ['B1', 'B2', 'R3']

def test_is_sorted():
    """Test sorting detection"""
    sorted_stacks = {
        'Red': ['R1', 'R2', 'R3'],
        'Blue': ['B1', 'B2', 'B3'],
        'Green': ['G1', 'G2', 'G3']
    }
    unsorted_stacks = {
        'Red': ['R1', 'R2'],
        'Blue': ['B1', 'B2', 'B3', 'R3'],
        'Green': ['G1', 'G2']
    }
    
    sorted_sorter = BallStackSorter(sorted_stacks)
    unsorted_sorter = BallStackSorter(unsorted_stacks)
    
    assert sorted_sorter.is_sorted() is True
    assert unsorted_sorter.is_sorted() is False

def test_sort():
    """Test complete sorting process"""
    stacks = {
        'Red': ['R1', 'R2', 'R3'],
        'Blue': ['B1', 'B2', 'G3'],
        'Green': ['B3', 'G1', 'G2']
    }
    sorter = BallStackSorter(stacks)
    
    states = sorter.sort()
    
    # Last state should be sorted
    final_state = states[-1]
    assert len(final_state['Red']) == 3
    assert len(final_state['Blue']) == 3
    assert len(final_state['Green']) == 3