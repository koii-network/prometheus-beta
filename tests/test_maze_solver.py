import pytest
from src.maze_solver import MazeSolver

class TestMazeSolver:
    def setup_method(self):
        """Initialize a MazeSolver for each test"""
        self.solver = MazeSolver()
    
    def test_simple_maze_with_path(self):
        """Test a simple maze with a clear path"""
        maze = [
            ['S', '0', '0', '0'],
            ['1', '1', '0', '1'],
            ['0', '0', '0', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is not None
        assert path[0] == (0, 0)  # Start point
        assert path[-1] == (2, 3)  # End point
    
    def test_maze_with_multiple_paths(self):
        """Test a maze with multiple possible paths"""
        maze = [
            ['S', '0', '1', '0'],
            ['1', '0', '1', '0'],
            ['0', '0', '0', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is not None
        assert len(path) == 6  # Actual shortest path length
        assert path[0] == (0, 0)  # Start point
        assert path[-1] == (2, 3)  # End point
    
    def test_maze_with_no_path(self):
        """Test a maze with no possible path"""
        maze = [
            ['S', '1', '1', '1'],
            ['1', '1', '1', '1'],
            ['1', '1', '1', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is None
    
    def test_empty_maze(self):
        """Test handling of an empty maze"""
        with pytest.raises(ValueError, match="Maze cannot be empty"):
            self.solver.find_shortest_path([])
    
    def test_maze_without_start_or_exit(self):
        """Test maze without start or exit points"""
        maze = [
            ['1', '1', '1'],
            ['1', '0', '1'],
            ['1', '1', '1']
        ]
        with pytest.raises(ValueError, match="Maze must have a start"):
            self.solver.find_shortest_path(maze)
    
    def test_single_cell_maze_with_path(self):
        """Test a single-cell maze with start and exit"""
        maze = [['S', 'E']]
        path = self.solver.find_shortest_path(maze)
        assert path == [(0, 0), (0, 1)]
    
    def test_complex_maze(self):
        """Test a more complex maze with obstacles"""
        maze = [
            ['S', '0', '1', '0', '0'],
            ['1', '0', '1', '0', '1'],
            ['0', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is not None
        assert path[0] == (0, 0)  # Start point
        assert path[-1] == (4, 4)  # End point