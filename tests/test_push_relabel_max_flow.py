import pytest
from src.push_relabel_max_flow import PushRelabelMaxFlow

def test_simple_graph():
    """Test a simple graph with known maximum flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    max_flow_solver = PushRelabelMaxFlow(graph, 0, 5)
    assert max_flow_solver.max_flow() == 19

def test_complete_single_path():
    """Test a graph with a single path from source to sink."""
    graph = {
        0: {1: 5},
        1: {2: 5},
        2: {}
    }
    max_flow_solver = PushRelabelMaxFlow(graph, 0, 2)
    assert max_flow_solver.max_flow() == 5

def test_disconnected_graph():
    """Test a graph with no path from source to sink."""
    graph = {
        0: {},
        1: {},
        2: {}
    }
    max_flow_solver = PushRelabelMaxFlow(graph, 0, 2)
    assert max_flow_solver.max_flow() == 0

def test_multiple_paths():
    """Test a graph with multiple paths from source to sink."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    max_flow_solver = PushRelabelMaxFlow(graph, 0, 5)
    assert max_flow_solver.max_flow() == 19

def test_large_capacities():
    """Test a graph with large capacity values."""
    graph = {
        0: {1: 1000000, 2: 1000000},
        1: {2: 1, 3: 1000000},
        2: {3: 1000000},
        3: {}
    }
    max_flow_solver = PushRelabelMaxFlow(graph, 0, 3)
    assert max_flow_solver.max_flow() == 1000001