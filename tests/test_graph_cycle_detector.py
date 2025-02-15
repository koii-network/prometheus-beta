import pytest
from src.graph_cycle_detector import detect_cycle_in_undirected_graph

def test_graph_with_cycle():
    # Graph with a cycle: 0 -> 1 -> 2 -> 0
    graph_with_cycle = {
        0: [1],
        1: [0, 2],
        2: [1, 0]
    }
    assert detect_cycle_in_undirected_graph(graph_with_cycle) == True

def test_graph_without_cycle():
    # Graph without a cycle: tree-like structure
    graph_without_cycle = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2]
    }
    assert detect_cycle_in_undirected_graph(graph_without_cycle) == False

def test_empty_graph():
    # Empty graph
    empty_graph = {}
    assert detect_cycle_in_undirected_graph(empty_graph) == False

def test_single_node_graph():
    # Single node graph
    single_node_graph = {0: []}
    assert detect_cycle_in_undirected_graph(single_node_graph) == False

def test_disconnected_graph_with_cycle():
    # Disconnected graph with a cycle
    disconnected_graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [4],
        4: [2]
    }
    assert detect_cycle_in_undirected_graph(disconnected_graph) == True