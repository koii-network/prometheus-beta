import pytest
from src.graph_cycle_detector import detect_cycle_in_undirected_graph

def test_graph_with_cycle():
    # Graph with a cycle: 0 -> 1 -> 2 -> 0
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    assert detect_cycle_in_undirected_graph(graph) == True

def test_graph_without_cycle():
    # Graph without a cycle: 0 -> 1 -> 2
    graph = {
        0: [1],
        1: [0, 2],
        2: [1]
    }
    assert detect_cycle_in_undirected_graph(graph) == False

def test_disconnected_graph_with_cycle():
    # Disconnected graph with a cycle
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2, 4],
        4: [3]
    }
    assert detect_cycle_in_undirected_graph(graph) == True

def test_disconnected_graph_without_cycle():
    # Disconnected graph without a cycle
    graph = {
        0: [1],
        1: [],
        2: [3],
        3: []
    }
    assert detect_cycle_in_undirected_graph(graph) == False

def test_single_node_graph():
    # Graph with a single node
    graph = {0: []}
    assert detect_cycle_in_undirected_graph(graph) == False

def test_empty_graph_raises_error():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError):
        detect_cycle_in_undirected_graph({})

def test_none_graph_raises_error():
    # None graph should raise ValueError
    with pytest.raises(ValueError):
        detect_cycle_in_undirected_graph(None)