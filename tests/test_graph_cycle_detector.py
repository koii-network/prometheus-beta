import pytest
from src.graph_cycle_detector import detect_cycle

def test_cycle_detection_with_cycle():
    """Test a graph with a cycle"""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    assert detect_cycle(graph) == True

def test_cycle_detection_without_cycle():
    """Test a graph without a cycle"""
    graph = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert detect_cycle(graph) == False

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {0: []}
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

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle({})

def test_none_graph_raises_error():
    """Test that a None graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle(None)  # type: ignore