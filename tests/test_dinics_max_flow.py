import pytest
from src.dinics_max_flow import DinicMaxFlow

def test_simple_max_flow():
    """
    Test a simple graph with a known max flow
    """
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 5)
    assert max_flow == 19

def test_disconnected_graph():
    """
    Test a graph with no path between source and sink
    """
    graph = {
        0: {1: 10},
        1: {0: 10},
        2: {3: 5},
        3: {2: 5}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 3)
    assert max_flow == 0

def test_invalid_source_sink():
    """
    Test handling of invalid source or sink nodes
    """
    graph = {
        0: {1: 10},
        1: {0: 10}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(2, 0)
    
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(0, 2)

def test_source_equals_sink():
    """
    Test when source and sink are the same node
    """
    graph = {
        0: {1: 10},
        1: {0: 10}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 0)
    assert max_flow == 0

def test_large_complex_graph():
    """
    Test a more complex graph with multiple paths
    """
    graph = {
        0: {1: 10, 2: 10, 3: 20},
        1: {2: 5, 4: 8, 5: 15},
        2: {3: 10, 5: 5},
        3: {6: 20},
        4: {5: 7, 6: 10},
        5: {6: 15},
        6: {}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 6)
    assert max_flow == 35