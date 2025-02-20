import pytest
from src.mall_navigation import find_shortest_path

def test_find_shortest_path_basic():
    mall_map = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 1, 'D': 3},
        'C': {'A': 5, 'B': 1, 'D': 6},
        'D': {'B': 3, 'C': 6}
    }
    
    path, distance = find_shortest_path(mall_map, 'A', 'D')
    assert path == ['A', 'B', 'D']
    assert distance == 5

def test_find_shortest_path_same_store():
    mall_map = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'C': 1},
        'C': {'A': 5, 'B': 1}
    }
    
    path, distance = find_shortest_path(mall_map, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_find_shortest_path_invalid_start_store():
    mall_map = {
        'A': {'B': 2},
        'B': {'A': 2}
    }
    
    with pytest.raises(ValueError, match="Start store 'X' not found in mall map"):
        find_shortest_path(mall_map, 'X', 'B')

def test_find_shortest_path_invalid_end_store():
    mall_map = {
        'A': {'B': 2},
        'B': {'A': 2}
    }
    
    with pytest.raises(ValueError, match="End store 'X' not found in mall map"):
        find_shortest_path(mall_map, 'A', 'X')

def test_find_shortest_path_no_path():
    mall_map = {
        'A': {'B': 2},
        'B': {'A': 2},
        'C': {'D': 1},
        'D': {'C': 1}
    }
    
    with pytest.raises(ValueError, match="No path found between A and C"):
        find_shortest_path(mall_map, 'A', 'C')