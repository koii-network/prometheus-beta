import pytest
from src.mall_navigation import find_shortest_path

def test_find_shortest_path_basic():
    mall_map = {
        'A': {'B': 5, 'C': 2},
        'B': {'A': 5, 'D': 4},
        'C': {'A': 2, 'D': 3},
        'D': {'B': 4, 'C': 3}
    }
    
    path, distance = find_shortest_path(mall_map, 'A', 'D')
    assert path == ['A', 'C', 'D']
    assert distance == 5

def test_find_shortest_path_same_store():
    mall_map = {
        'A': {'B': 5, 'C': 2},
        'B': {'A': 5, 'D': 4},
        'C': {'A': 2, 'D': 3},
        'D': {'B': 4, 'C': 3}
    }
    
    path, distance = find_shortest_path(mall_map, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_find_shortest_path_no_direct_connection():
    mall_map = {
        'A': {'B': 5},
        'B': {'A': 5, 'C': 3},
        'C': {'B': 3}
    }
    
    path, distance = find_shortest_path(mall_map, 'A', 'C')
    assert path == ['A', 'B', 'C']
    assert distance == 8

def test_find_shortest_path_non_existent_start():
    mall_map = {
        'A': {'B': 5},
        'B': {'A': 5, 'C': 3},
        'C': {'B': 3}
    }
    
    with pytest.raises(ValueError, match="Start store 'D' not found in mall map"):
        find_shortest_path(mall_map, 'D', 'A')

def test_find_shortest_path_non_existent_end():
    mall_map = {
        'A': {'B': 5},
        'B': {'A': 5, 'C': 3},
        'C': {'B': 3}
    }
    
    with pytest.raises(ValueError, match="End store 'D' not found in mall map"):
        find_shortest_path(mall_map, 'A', 'D')

def test_find_shortest_path_disconnected_stores():
    mall_map = {
        'A': {'B': 5},
        'B': {'A': 5},
        'C': {'D': 3},
        'D': {'C': 3}
    }
    
    with pytest.raises(ValueError, match="No path exists between 'A' and 'C'"):
        find_shortest_path(mall_map, 'A', 'C')