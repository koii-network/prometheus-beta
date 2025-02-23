import pytest
from src.mall_navigation import find_shortest_path

def test_basic_shortest_path():
    mall_graph = {
        'A': {'B': 5, 'C': 2},
        'B': {'A': 5, 'C': 1, 'D': 3},
        'C': {'A': 2, 'B': 1, 'D': 6},
        'D': {'B': 3, 'C': 6}
    }
    path, distance = find_shortest_path(mall_graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4

def test_direct_path():
    mall_graph = {
        'A': {'B': 3, 'C': 10},
        'B': {'A': 3, 'C': 2},
        'C': {'A': 10, 'B': 2}
    }
    path, distance = find_shortest_path(mall_graph, 'A', 'B')
    assert path == ['A', 'B']
    assert distance == 3

def test_single_store_path():
    mall_graph = {
        'A': {}
    }
    path, distance = find_shortest_path(mall_graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_start_store_not_in_graph():
    mall_graph = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    with pytest.raises(ValueError, match="Start store 'C' not found in mall graph"):
        find_shortest_path(mall_graph, 'C', 'A')

def test_end_store_not_in_graph():
    mall_graph = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    with pytest.raises(ValueError, match="End store 'C' not found in mall graph"):
        find_shortest_path(mall_graph, 'A', 'C')

def test_no_path_exists():
    mall_graph = {
        'A': {},
        'B': {}
    }
    with pytest.raises(ValueError, match="No path exists between 'A' and 'B'"):
        find_shortest_path(mall_graph, 'A', 'B')