import pytest
from src.ball_stack_sorter import BallStackSorter

def test_basic_sorting():
    # Test case with unbalanced, mixed color stacks
    initial_stacks = {
        'Red': ['Red', 'Blue', 'Green'],
        'Blue': ['Green', 'Red', 'Blue'],
        'Green': ['Blue', 'Green', 'Red']
    }
    sorter = BallStackSorter(initial_stacks)
    moves = sorter.sort_stacks()
    
    assert sorter.is_sorted()
    assert len(moves) > 0

def test_already_sorted_stacks():
    # Test case where stacks are already sorted
    initial_stacks = {
        'Red': ['Red', 'Red', 'Red'],
        'Blue': ['Blue', 'Blue', 'Blue'],
        'Green': ['Green', 'Green', 'Green']
    }
    sorter = BallStackSorter(initial_stacks)
    moves = sorter.sort_stacks()
    
    assert sorter.is_sorted()
    assert len(moves) == 0

def test_is_sorted_method():
    # Test is_sorted method for various scenarios
    sorted_stacks = {
        'Red': ['Red', 'Red', 'Red'],
        'Blue': ['Blue', 'Blue', 'Blue'],
        'Green': ['Green', 'Green', 'Green']
    }
    unsorted_stacks1 = {
        'Red': ['Red', 'Blue', 'Green'],
        'Blue': ['Green', 'Red', 'Blue'],
        'Green': ['Blue', 'Green', 'Red']
    }
    unsorted_stacks2 = {
        'Red': ['Red', 'Red', 'Red', 'Blue'],
        'Blue': ['Blue', 'Blue', 'Blue'],
        'Green': ['Green', 'Green', 'Green']
    }
    
    sorted_sorter = BallStackSorter(sorted_stacks)
    unsorted_sorter1 = BallStackSorter(unsorted_stacks1)
    unsorted_sorter2 = BallStackSorter(unsorted_stacks2)
    
    assert sorted_sorter.is_sorted() == True
    assert unsorted_sorter1.is_sorted() == False
    assert unsorted_sorter2.is_sorted() == False

def test_move_ball():
    # Test moving a ball between stacks
    initial_stacks = {
        'Red': ['Red', 'Blue'],
        'Blue': ['Green'],
        'Green': []
    }
    sorter = BallStackSorter(initial_stacks)
    sorter.move_ball('Red', 'Green')
    
    assert sorter.stacks['Red'] == ['Red']
    assert sorter.stacks['Green'] == ['Blue']

def test_move_ball_empty_source():
    # Test moving from an empty stack raises an error
    initial_stacks = {
        'Red': [],
        'Blue': ['Blue'],
        'Green': ['Green']
    }
    sorter = BallStackSorter(initial_stacks)
    
    with pytest.raises(ValueError):
        sorter.move_ball('Red', 'Blue')