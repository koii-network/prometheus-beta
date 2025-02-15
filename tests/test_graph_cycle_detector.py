import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_with_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: [1]  # Creates a cycle
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_graph_without_cycle():
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_no_cycle():
    graph = {0: []}
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_self_cycle():
    graph = {0: [0]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_multiple_node_self_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [2]  # Self cycle
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_complex_cycle():
    graph = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [4, 5],
        4: [1],  # Back to node 1, creating a cycle
        5: []
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_empty_graph_raises_error():
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph({})

def test_none_graph_raises_error():
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph(None)