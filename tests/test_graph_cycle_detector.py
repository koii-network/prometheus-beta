import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_with_no_cycle():
    """Test a graph with no cycles"""
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) is False

def test_graph_with_simple_cycle():
    """Test a graph with a simple cycle"""
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    assert detect_cycle_in_directed_graph(graph) is True

def test_graph_with_complex_cycle():
    """Test a graph with a more complex cycle"""
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1, 4],
        4: []
    }
    assert detect_cycle_in_directed_graph(graph) is True

def test_empty_graph():
    """Test an empty graph"""
    graph = {}
    assert detect_cycle_in_directed_graph(graph) is False

def test_single_node_graph():
    """Test a graph with a single node with no edges"""
    graph = {0: []}
    assert detect_cycle_in_directed_graph(graph) is False

def test_single_node_self_cycle():
    """Test a graph with a single node pointing to itself"""
    graph = {0: [0]}
    assert detect_cycle_in_directed_graph(graph) is True

def test_disconnected_graph_with_cycle():
    """Test a disconnected graph with a cycle in one component"""
    graph = {
        0: [1],
        1: [2],
        2: [0],
        3: [4],
        4: [5],
        5: [3]
    }
    assert detect_cycle_in_directed_graph(graph) is True

def test_graph_with_long_cycle():
    """Test a graph with a long cycle"""
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: [0]
    }
    assert detect_cycle_in_directed_graph(graph) is True

def test_invalid_input_none():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph(None)

def test_graph_with_unreachable_nodes():
    """Test a graph with unreachable nodes"""
    graph = {
        0: [1],
        1: [2],
        2: [],
        3: [4],
        4: [5],
        5: [3]
    }
    assert detect_cycle_in_directed_graph(graph) is True