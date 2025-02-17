import pytest
from src.graph_cycle_detector import detect_cycle

def test_graph_with_cycle():
    # Graph with a cycle
    graph1 = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    assert detect_cycle(graph1) == True

def test_graph_without_cycle():
    # Graph without a cycle (tree-like structure)
    graph2 = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [],
        5: []
    }
    assert detect_cycle(graph2) == False

def test_disconnected_graph_with_cycle():
    # Disconnected graph with a cycle
    graph3 = {
        0: [1],
        1: [0],
        2: [3],
        3: [4],
        4: [2]
    }
    assert detect_cycle(graph3) == True

def test_disconnected_graph_without_cycle():
    # Disconnected graph without a cycle
    graph4 = {
        0: [1],
        1: [],
        2: [3],
        3: []
    }
    assert detect_cycle(graph4) == False

def test_single_node_graph():
    # Single node graph (no cycle)
    graph5 = {0: []}
    assert detect_cycle(graph5) == False

def test_empty_graph():
    # Empty graph should raise a ValueError
    with pytest.raises(ValueError):
        detect_cycle({})

def test_complex_graph_with_multiple_cycles():
    # Complex graph with multiple cycles
    graph6 = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }
    assert detect_cycle(graph6) == True