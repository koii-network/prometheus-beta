import pytest
from src.push_relabel_max_flow import push_relabel_max_flow

def test_simple_graph():
    """Test a simple graph with a known maximum flow"""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert push_relabel_max_flow(graph, 0, 5) == 14

def test_disconnected_graph():
    """Test a graph with no path from source to sink"""
    graph = {
        0: {1: 5},
        1: {0: 5},
        2: {3: 10},
        3: {2: 10}
    }
    assert push_relabel_max_flow(graph, 0, 3) == 0

def test_complex_graph():
    """Test a more complex graph with multiple paths"""
    graph = {
        0: {1: 3, 2: 3, 3: 3},
        1: {2: 4, 4: 4},
        2: {3: 1, 4: 2},
        3: {5: 2},
        4: {5: 5},
        5: {}
    }
    assert push_relabel_max_flow(graph, 0, 5) == 5

def test_single_edge_graph():
    """Test a graph with just one edge"""
    graph = {
        0: {1: 42},
        1: {}
    }
    assert push_relabel_max_flow(graph, 0, 1) == 42

def test_zero_capacity_graph():
    """Test a graph with zero-capacity edges"""
    graph = {
        0: {1: 0, 2: 0},
        1: {2: 0},
        2: {}
    }
    assert push_relabel_max_flow(graph, 0, 2) == 0

def test_invalid_source_sink():
    """Test with invalid source or sink"""
    graph = {
        0: {1: 10},
        1: {}
    }
    # Source and sink not in the graph
    assert push_relabel_max_flow(graph, 2, 3) == 0

def test_same_source_and_sink():
    """Test with source and sink being the same node"""
    graph = {
        0: {1: 10},
        1: {}
    }
    assert push_relabel_max_flow(graph, 0, 0) == 0