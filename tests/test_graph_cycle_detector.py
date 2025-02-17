import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_with_cycle():
    # Graph with a cycle: 0 -> 1 -> 2 -> 0
    graph_with_cycle = {
        0: [1],
        1: [2],
        2: [0]
    }
    assert detect_cycle_in_directed_graph(graph_with_cycle) == True

def test_graph_without_cycle():
    # Graph without a cycle
    graph_without_cycle = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph_without_cycle) == False

def test_single_node_with_self_loop():
    # Single node pointing to itself (self-loop)
    graph_with_self_loop = {
        0: [0]
    }
    assert detect_cycle_in_directed_graph(graph_with_self_loop) == True

def test_complex_graph_with_cycle():
    # More complex graph with a cycle
    graph_with_complex_cycle = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [5],
        4: [1, 5],
        5: []
    }
    assert detect_cycle_in_directed_graph(graph_with_complex_cycle) == True

def test_complex_graph_without_cycle():
    # Complex graph without a cycle
    graph_without_cycle = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [5],
        4: [5],
        5: []
    }
    assert detect_cycle_in_directed_graph(graph_without_cycle) == False

def test_empty_graph_raises_error():
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph({})

def test_none_graph_raises_error():
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph(None)