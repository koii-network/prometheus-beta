import pytest
from src.graph_cycle_detection import detect_cycle

def test_cycle_in_simple_graph():
    """Test a graph with a cycle"""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    assert detect_cycle(graph) == True

def test_cycle_in_complex_graph():
    """Test a more complex graph with a cycle"""
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1, 4],
        4: [2, 3]
    }
    assert detect_cycle(graph) == True

def test_graph_without_cycle():
    """Test a graph without a cycle"""
    graph = {
        0: [1, 2],
        1: [0],
        2: [0, 3],
        3: [2]
    }
    assert detect_cycle(graph) == False

def test_disconnected_graph_with_cycle():
    """Test a disconnected graph with a cycle"""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [4],
        4: [2]
    }
    assert detect_cycle(graph) == True

def test_disconnected_graph_without_cycle():
    """Test a disconnected graph without a cycle"""
    graph = {
        0: [1],
        1: [],
        2: [3],
        3: []
    }
    assert detect_cycle(graph) == False

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {0: []}
    assert detect_cycle(graph) == False

def test_two_node_connected_graph():
    """Test a graph with two connected nodes"""
    graph = {
        0: [1],
        1: [0]
    }
    assert detect_cycle(graph) == True

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle({})

def test_none_graph_raises_error():
    """Test that a None graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle(None)