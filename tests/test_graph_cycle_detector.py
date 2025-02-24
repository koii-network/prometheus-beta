import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_with_no_cycle():
    """Test a graph with no cycle."""
    graph = {
        0: [1, 2],
        1: [2],
        2: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_graph_with_simple_cycle():
    """Test a graph with a simple cycle."""
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_graph_with_complex_cycle():
    """Test a graph with a more complex cycle."""
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_empty_graph():
    """Test an empty graph."""
    graph = {}
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_graph():
    """Test a graph with a single node with no self-loop."""
    graph = {0: []}
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_self_loop():
    """Test a graph with a single node that has a self-loop."""
    graph = {0: [0]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_disconnected_graph_with_cycle():
    """Test a disconnected graph with a cycle."""
    graph = {
        0: [1],
        1: [2],
        2: [0],
        3: [4],
        4: [5],
        5: [3]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_raises_error_for_none_input():
    """Test that the function raises a ValueError for None input."""
    with pytest.raises(ValueError, match="Graph cannot be None"):
        detect_cycle_in_directed_graph(None)

def test_graph_with_multiple_paths():
    """Test a graph with multiple paths but no cycle."""
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) == False