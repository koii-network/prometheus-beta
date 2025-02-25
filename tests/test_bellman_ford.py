import pytest
from src.bellman_ford import bellman_ford


def test_basic_graph():
    """Test a simple graph with known shortest paths."""
    graph = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 5)
    ]
    num_vertices = 4
    start = 0

    result = bellman_ford(graph, start, num_vertices)
    assert result is not None
    assert result[0] == 0
    assert result[1] == 4
    assert result[2] == 3
    assert result[3] == 6


def test_disconnected_vertex():
    """Test graph with a disconnected vertex."""
    graph = [
        (0, 1, 4),
        (0, 2, 3)
    ]
    num_vertices = 4
    start = 0

    result = bellman_ford(graph, start, num_vertices)
    assert result is not None
    assert result[0] == 0
    assert result[1] == 4
    assert result[2] == 3
    assert result[3] == float('inf')


def test_negative_weights():
    """Test graph with negative edge weights."""
    graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (2, 3, 5)
    ]
    num_vertices = 4
    start = 0

    result = bellman_ford(graph, start, num_vertices)
    assert result is not None
    assert result[0] == 0
    assert result[1] == -1
    assert result[2] == 2
    assert result[3] == 1


def test_negative_cycle():
    """Test graph with a negative weight cycle."""
    graph = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 0, -2)
    ]
    num_vertices = 3
    start = 0

    result = bellman_ford(graph, start, num_vertices)
    assert result is None


def test_single_vertex():
    """Test graph with single vertex."""
    graph = []
    num_vertices = 1
    start = 0

    result = bellman_ford(graph, start, num_vertices)
    assert result is not None
    assert result[0] == 0


def test_invalid_inputs():
    """Test invalid input handling."""
    # Empty graph
    with pytest.raises(ValueError):
        bellman_ford([], 0, 1)

    # Negative start vertex
    with pytest.raises(ValueError):
        bellman_ford([(0, 1, 1)], -1, 2)

    # Invalid number of vertices
    with pytest.raises(ValueError):
        bellman_ford([(0, 1, 1)], 0, 0)


def test_large_graph():
    """Test performance with a larger graph."""
    graph = [
        (0, 1, 5),
        (0, 2, 2),
        (1, 3, 4),
        (1, 4, 2),
        (2, 1, 1),
        (2, 3, 7),
        (3, 4, 3),
        (4, 0, 6)
    ]
    num_vertices = 5
    start = 0

    result = bellman_ford(graph, start, num_vertices)
    assert result is not None
    assert len(result) == 5