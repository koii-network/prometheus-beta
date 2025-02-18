import pytest
from src.push_relabel_max_flow import PushRelabelMaxFlow

def test_simple_max_flow():
    """
    Test a simple graph with a known maximum flow
    """
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {4: 10, 5: 10},
        4: {5: 10},
        5: {}
    }
    
    max_flow_solver = PushRelabelMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 5)
    
    assert max_flow == 19, f"Expected max flow of 19, got {max_flow}"

def test_disconnected_graph():
    """
    Test a graph where source and sink are disconnected
    """
    graph = {
        0: {1: 5},
        1: {0: 0},
        2: {3: 10},
        3: {2: 0}
    }
    
    max_flow_solver = PushRelabelMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 3)
    
    assert max_flow == 0, f"Expected max flow of 0, got {max_flow}"

def test_single_path_graph():
    """
    Test a simple linear graph
    """
    graph = {
        0: {1: 5},
        1: {2: 5},
        2: {3: 5},
        3: {}
    }
    
    max_flow_solver = PushRelabelMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 3)
    
    assert max_flow == 5, f"Expected max flow of 5, got {max_flow}"

def test_invalid_vertices():
    """
    Test error handling for invalid source or sink
    """
    graph = {
        0: {1: 10},
        1: {0: 0}
    }
    
    max_flow_solver = PushRelabelMaxFlow(graph)
    
    with pytest.raises(ValueError, match="Source or sink not in graph"):
        max_flow_solver.max_flow(2, 1)
    
    with pytest.raises(ValueError, match="Source or sink not in graph"):
        max_flow_solver.max_flow(0, 2)

def test_same_source_and_sink():
    """
    Test when source and sink are the same vertex
    """
    graph = {
        0: {1: 10},
        1: {0: 0}
    }
    
    max_flow_solver = PushRelabelMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 0)
    
    assert max_flow == 0, f"Expected max flow of 0, got {max_flow}"

def test_complex_multi_path_graph():
    """
    Test a more complex graph with multiple paths
    """
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {4: 10, 5: 10},
        4: {5: 10},
        5: {}
    }
    
    max_flow_solver = PushRelabelMaxFlow(graph)
    max_flow = max_flow_solver.max_flow(0, 5)
    
    assert max_flow == 19, f"Expected max flow of 19, got {max_flow}"