import pytest
from src.boruvka_mst import boruvka_mst, DisjointSet

class TestDisjointSet:
    def test_initial_parent(self):
        ds = DisjointSet(5)
        assert ds.parent == [0, 1, 2, 3, 4]

    def test_find(self):
        ds = DisjointSet(5)
        assert ds.find(2) == 2

    def test_union(self):
        ds = DisjointSet(5)
        assert ds.union(0, 1) == True
        assert ds.find(0) == ds.find(1)
        assert ds.union(0, 1) == False  # Already in same set

class TestBoruvkaMST:
    def test_empty_graph(self):
        assert boruvka_mst(0, []) == []

    def test_single_vertex(self):
        assert boruvka_mst(1, []) == []

    def test_valid_mst(self):
        # Graph with multiple vertices and edges
        edges = [
            (1, 0, 1),
            (3, 1, 2),
            (4, 0, 2),
            (2, 1, 3),
            (5, 2, 3)
        ]
        mst = boruvka_mst(4, edges)
        
        # Check that number of edges is (vertices - 1)
        assert len(mst) == 3

        # Total weight of MST
        total_weight = sum(edge[0] for edge in mst)
        assert total_weight == 6

    def test_disconnected_graph(self):
        # Disconnected graph should raise an error or return partial MST
        edges = [
            (1, 0, 1),
            (3, 2, 3)
        ]
        with pytest.raises(Exception):
            boruvka_mst(4, edges)

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            boruvka_mst(-1, [])

    def test_mst_smallest_weight(self):
        # Ensure algorithm picks smallest total weight
        edges = [
            (10, 0, 1),
            (6, 1, 2),
            (5, 0, 2)
        ]
        mst = boruvka_mst(3, edges)
        total_weight = sum(edge[0] for edge in mst)
        assert total_weight == 11

    def test_complex_graph(self):
        # More complex graph to test multiple iterations
        edges = [
            (1, 0, 1), (2, 1, 2), (3, 0, 2),
            (4, 1, 3), (5, 2, 3), (6, 2, 4),
            (7, 3, 4)
        ]
        mst = boruvka_mst(5, edges)
        
        # Check that number of edges is (vertices - 1)
        assert len(mst) == 4

        # Verify weights are minimal
        total_weight = sum(edge[0] for edge in mst)
        assert total_weight == 10