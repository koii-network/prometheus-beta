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

def test_empty_graph_raises_exception():
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph({})

def test_none_graph_raises_exception():
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph(None)

def test_isolated_nodes_graph():
    graph = {
        1: [],
        2: [],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_self_referencing_cycle():
    graph = {
        1: [1]
    }
    assert detect_cycle_in_directed_graph(graph) == True