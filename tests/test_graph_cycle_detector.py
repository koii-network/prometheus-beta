import pytest
from src.graph_cycle_detector import detect_cycle_in_undirected_graph

def test_graph_with_cycle():
    """Test a graph that contains a cycle"""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    assert detect_cycle_in_undirected_graph(graph) == True

def test_graph_without_cycle():
    """Test a graph without a cycle"""
    graph = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2]
    }
    assert detect_cycle_in_undirected_graph(graph) == False

def test_disconnected_graph_with_cycle():
    """Test a disconnected graph that contains a cycle"""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [4],
        4: [2, 3]
    }
    assert detect_cycle_in_undirected_graph(graph) == True

def test_disconnected_graph_without_cycle():
    """Test a disconnected graph without a cycle"""
    graph = {
        0: [1],
        1: [2],
        2: [],
        3: [4],
        4: []
    }
    assert detect_cycle_in_undirected_graph(graph) == False

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {0: []}
    assert detect_cycle_in_undirected_graph(graph) == False

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle_in_undirected_graph({})

def test_none_graph_raises_error():
    """Test that a None graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle_in_undirected_graph(None)  # type: ignore