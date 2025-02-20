import pytest
from src.mall_navigation import find_shortest_path

def test_simple_path():
    mall_map = {
        'A': {'B': 5, 'C': 2},
        'B': {'A': 5, 'D': 4},
        'C': {'A': 2, 'D': 6},
        'D': {'B': 4, 'C': 6}
    }
    path, distance = find_shortest_path(mall_map, 'A', 'D')
    assert path == ['A', 'C', 'D']
    assert distance == 8

def test_same_start_and_end():
    mall_map = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    path, distance = find_shortest_path(mall_map, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_non_existent_start_store():
    mall_map = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    with pytest.raises(ValueError, match="Start store 'C' not found in mall map"):
        find_shortest_path(mall_map, 'C', 'A')

def test_non_existent_end_store():
    mall_map = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    with pytest.raises(ValueError, match="End store 'C' not found in mall map"):
        find_shortest_path(mall_map, 'A', 'C')

def test_no_path_exists():
    mall_map = {
        'A': {},
        'B': {},
        'C': {}
    }
    with pytest.raises(ValueError, match="No path exists between 'A' and 'B'"):
        find_shortest_path(mall_map, 'A', 'B')

def test_complex_path():
    mall_map = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 3},
        'C': {'A': 2, 'D': 5, 'E': 6},
        'D': {'B': 3, 'C': 5, 'E': 2},
        'E': {'C': 6, 'D': 2}
    }
    path, distance = find_shortest_path(mall_map, 'A', 'E')
    
    # All valid paths
    valid_paths = [
        ['A', 'C', 'E'],
        ['A', 'C', 'D', 'E']
    ]
    assert path in valid_paths
    assert path == ['A', 'C', 'E'] or path == ['A', 'C', 'D', 'E']