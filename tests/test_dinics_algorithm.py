import pytest
from src.dinics_algorithm import Dinic

def test_dinic_simple_graph():
    # Simple graph with one path
    graph = {
        0: {1: 10},
        1: {2: 10},
        2: {}
    }
    dinic = Dinic(graph)
    assert dinic.max_flow(0, 2) == 10

def test_dinic_complex_graph():
    # More complex graph with multiple paths
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    dinic = Dinic(graph)
    assert dinic.max_flow(0, 5) == 19

def test_dinic_no_flow():
    # Graph with no possible flow
    graph = {
        0: {},
        1: {}
    }
    dinic = Dinic(graph)
    assert dinic.max_flow(0, 1) == 0

def test_dinic_invalid_vertices():
    # Test with vertices not in graph
    graph = {
        0: {1: 10},
        1: {}
    }
    dinic = Dinic(graph)
    
    with pytest.raises(ValueError):
        dinic.max_flow(2, 1)
    
    with pytest.raises(ValueError):
        dinic.max_flow(0, 2)

def test_dinic_zero_capacity_graph():
    # Graph with zero capacity edges
    graph = {
        0: {1: 0, 2: 0},
        1: {2: 0},
        2: {}
    }
    dinic = Dinic(graph)
    assert dinic.max_flow(0, 2) == 0