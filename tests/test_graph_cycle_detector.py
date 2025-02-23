import pytest
from src.graph_cycle_detector import detect_cycle_in_undirected_graph

def test_cycle_detection():
    # Graph with a cycle
    graph_with_cycle = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    assert detect_cycle_in_undirected_graph(graph_with_cycle) == True

def test_graph_without_cycle():
    # Graph without a cycle
    graph_without_cycle = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2]
    }
    assert detect_cycle_in_undirected_graph(graph_without_cycle) == False

def test_disconnected_graph_with_cycle():
    # Disconnected graph with a cycle in one component
    graph_disconnected_with_cycle = {
        0: [1],
        1: [0],
        2: [3, 4],
        3: [2, 4],
        4: [2, 3]
    }
    assert detect_cycle_in_undirected_graph(graph_disconnected_with_cycle) == True

def test_disconnected_graph_without_cycle():
    # Disconnected graph without a cycle
    graph_disconnected_without_cycle = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    assert detect_cycle_in_undirected_graph(graph_disconnected_without_cycle) == False

def test_single_node_graph():
    # Single node graph
    graph_single_node = {
        0: []
    }
    assert detect_cycle_in_undirected_graph(graph_single_node) == False

def test_empty_graph_raises_error():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError):
        detect_cycle_in_undirected_graph({})

def test_complex_graph_with_multiple_cycles():
    # Complex graph with multiple cycles
    graph_complex_cycles = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }
    assert detect_cycle_in_undirected_graph(graph_complex_cycles) == True