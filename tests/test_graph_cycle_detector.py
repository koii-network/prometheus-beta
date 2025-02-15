import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_with_no_cycle():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_graph_with_simple_cycle():
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_graph_with_complex_cycle():
    graph = {
        1: [2],
        2: [3, 4],
        3: [4, 5],
        4: [1],
        5: []
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_graph_with_single_node_self_cycle():
    graph = {
        1: [1]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_empty_graph_raises_error():
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph({})

def test_disconnected_graph_with_cycle():
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4]
    }
    assert detect_cycle_in_directed_graph(graph) == True