import pytest
from src.push_relabel_max_flow import PushRelabelMaxFlow

def test_basic_max_flow():
    """
    Test a simple max flow scenario
    """
    # Create a graph with 4 vertices
    max_flow_solver = PushRelabelMaxFlow(4)
    
    # Add edges
    max_flow_solver.add_edge(0, 1, 10)
    max_flow_solver.add_edge(0, 2, 8)
    max_flow_solver.add_edge(1, 2, 2)
    max_flow_solver.add_edge(1, 3, 4)
    max_flow_solver.add_edge(2, 3, 8)
    
    # Compute max flow from source (0) to sink (3)
    flow = max_flow_solver.max_flow(0, 3)
    
    # Expected max flow is 12
    assert flow == 12

def test_linear_graph():
    """
    Test max flow in a linear graph
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    
    # Linear graph with decreasing capacities
    max_flow_solver.add_edge(0, 1, 5)
    max_flow_solver.add_edge(1, 2, 3)
    
    # Compute max flow
    flow = max_flow_solver.max_flow(0, 2)
    
    # Expected max flow is 3
    assert flow == 3

def test_no_flow_graph():
    """
    Test a graph with no possible flow
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    
    # No edges between source and sink
    
    # Compute max flow
    flow = max_flow_solver.max_flow(0, 2)
    
    # Expected max flow is 0
    assert flow == 0

def test_complete_graph():
    """
    Test a more complex max flow scenario
    """
    max_flow_solver = PushRelabelMaxFlow(6)
    
    # Add complex set of edges
    max_flow_solver.add_edge(0, 1, 10)
    max_flow_solver.add_edge(0, 2, 10)
    max_flow_solver.add_edge(1, 3, 4)
    max_flow_solver.add_edge(1, 4, 8)
    max_flow_solver.add_edge(2, 4, 9)
    max_flow_solver.add_edge(3, 5, 10)
    max_flow_solver.add_edge(4, 5, 10)
    
    # Compute max flow
    flow = max_flow_solver.max_flow(0, 5)
    
    # Expected max flow depends on the graph structure
    assert flow == 14

def test_invalid_source_or_sink():
    """
    Test error handling for invalid source or sink
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    
    # Test out of bounds source
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(-1, 2)
    
    # Test out of bounds sink
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(0, 3)
    
    # Test source equals sink
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(1, 1)

def test_single_vertex_graph():
    """
    Test graph with only one vertex
    """
    max_flow_solver = PushRelabelMaxFlow(1)
    
    # Compute max flow
    flow = max_flow_solver.max_flow(0, 0)
    
    # Expected max flow is 0
    assert flow == 0