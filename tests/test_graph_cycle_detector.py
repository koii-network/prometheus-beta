import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_cycle_detection_with_cycle():
    """Test graph with a direct cycle"""
    graph = {
        1: [2],
        2: [3],
        3: [1]  # Cycle: 1 -> 2 -> 3 -> 1
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_cycle_detection_with_indirect_cycle():
    """Test graph with an indirect cycle"""
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [2]  # Cycle: 2 -> 3 -> 4 -> 2
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_cycle_detection_without_cycle():
    """Test graph without a cycle"""
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_graph():
    """Test graph with a single node pointing to itself"""
    graph = {
        1: [1]  # Self-loop cycle
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        detect_cycle_in_directed_graph({})

def test_disconnected_graph_with_cycle():
    """Test a disconnected graph that contains a cycle"""
    graph = {
        1: [2],
        2: [3],
        3: [1],  # Cycle in first component
        4: [5],
        5: [6],
        6: [4]   # Cycle in second component
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_disconnected_graph_without_cycle():
    """Test a disconnected graph without a cycle"""
    graph = {
        1: [2],
        2: [3],
        3: [],
        4: [5],
        5: [6],
        6: []
    }
    assert detect_cycle_in_directed_graph(graph) == False