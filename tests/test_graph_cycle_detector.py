import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_cycle_detection():
    # Test cases with cycles
    cycle_graphs = [
        {0: [1], 1: [2], 2: [0]},  # Simple 3-node cycle
        {0: [1], 1: [2], 2: [3], 3: [1]},  # Cycle through multiple nodes
        {0: [1, 2], 1: [2], 2: [0]},  # Multiple paths with a cycle
    ]
    
    # Test cases without cycles
    non_cycle_graphs = [
        {0: [1], 1: [2], 2: [3]},  # Linear graph
        {0: [], 1: [], 2: []},  # Disconnected graph
        {},  # Empty graph
    ]
    
    # Test graphs with cycles
    for graph in cycle_graphs:
        assert detect_cycle_in_directed_graph(graph) is True, f"Failed to detect cycle in {graph}"
    
    # Test graphs without cycles
    for graph in non_cycle_graphs:
        assert detect_cycle_in_directed_graph(graph) is False, f"Incorrectly detected cycle in {graph}"

def test_large_graph():
    # Large graph with no cycle
    large_graph = {
        0: [1, 2],
        1: [3, 4],
        2: [4, 5],
        3: [6],
        4: [6],
        5: [6],
        6: []
    }
    assert detect_cycle_in_directed_graph(large_graph) is False

def test_large_graph_with_cycle():
    # Large graph with a complex cycle
    large_graph_with_cycle = {
        0: [1, 2],
        1: [3, 4],
        2: [4, 5],
        3: [6],
        4: [6, 1],  # Cycle introduced here
        5: [6],
        6: []
    }
    assert detect_cycle_in_directed_graph(large_graph_with_cycle) is True

def test_self_loop():
    # Graph with self-loop
    self_loop_graph = {0: [0]}
    assert detect_cycle_in_directed_graph(self_loop_graph) is True