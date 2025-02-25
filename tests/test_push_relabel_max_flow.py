import pytest
from src.push_relabel_max_flow import PushRelabelMaxFlow

def test_basic_max_flow():
    """
    Test a simple graph with known max flow.
    """
    # Create a graph with 4 vertices
    max_flow_solver = PushRelabelMaxFlow(4)
    
    # Add edges
    max_flow_solver.add_edge(0, 1, 10)
    max_flow_solver.add_edge(0, 2, 8)
    max_flow_solver.add_edge(1, 2, 2)
    max_flow_solver.add_edge(1, 3, 5)
    max_flow_solver.add_edge(2, 3, 10)
    
    # Calculate max flow from source (0) to sink (3)
    result = max_flow_solver.max_flow(0, 3)
    
    # Expected max flow is 15
    assert result == 15

def test_single_path_max_flow():
    """
    Test a graph with a single direct path.
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    max_flow_solver.add_edge(0, 1, 5)
    max_flow_solver.add_edge(1, 2, 5)
    
    result = max_flow_solver.max_flow(0, 2)
    assert result == 5

def test_no_path_max_flow():
    """
    Test a graph with no path between source and sink.
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    max_flow_solver.add_edge(0, 1, 5)
    # No edge to sink
    
    result = max_flow_solver.max_flow(0, 2)
    assert result == 0

def test_complex_max_flow():
    """
    Test a more complex graph with multiple paths.
    """
    max_flow_solver = PushRelabelMaxFlow(6)
    
    # More complex graph edges
    max_flow_solver.add_edge(0, 1, 10)
    max_flow_solver.add_edge(0, 2, 10)
    max_flow_solver.add_edge(1, 3, 4)
    max_flow_solver.add_edge(1, 4, 8)
    max_flow_solver.add_edge(2, 3, 5)
    max_flow_solver.add_edge(2, 4, 8)
    max_flow_solver.add_edge(3, 5, 6)
    max_flow_solver.add_edge(4, 5, 10)
    
    result = max_flow_solver.max_flow(0, 5)
    assert result == 16  # Sum of flows through different paths

def test_invalid_input():
    """
    Test handling of invalid graph configurations.
    """
    with pytest.raises(Exception):
        # Attempt to find max flow to same vertex
        max_flow_solver = PushRelabelMaxFlow(2)
        max_flow_solver.max_flow(0, 0)