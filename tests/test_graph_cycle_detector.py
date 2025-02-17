import pytest
from src.graph_cycle_detector import detect_cycle_in_undirected_graph

def test_graph_with_cycle():
    # Graph with a cycle
    graph_with_cycle = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    assert detect_cycle_in_undirected_graph(graph_with_cycle) == True

def test_graph_without_cycle():
    # Graph without a cycle (tree-like structure)
    graph_without_cycle = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [],
        5: []
    }
    assert detect_cycle_in_undirected_graph(graph_without_cycle) == False

def test_empty_graph():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError):
        detect_cycle_in_undirected_graph({})

def test_single_node_graph():
    # Single node graph has no cycle
    single_node_graph = {0: []}
    assert detect_cycle_in_undirected_graph(single_node_graph) == False

def test_two_node_graph_no_cycle():
    # Two nodes without connection
    two_node_graph_no_cycle = {0: [], 1: []}
    assert detect_cycle_in_undirected_graph(two_node_graph_no_cycle) == False

def test_two_node_graph_with_cycle():
    # Two nodes connected to each other
    two_node_graph_with_cycle = {0: [1], 1: [0]}
    assert detect_cycle_in_undirected_graph(two_node_graph_with_cycle) == True