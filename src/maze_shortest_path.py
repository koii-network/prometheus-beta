from typing import List, Tuple
import heapq

def find_shortest_path(maze: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find the shortest path through a maze from top-left to bottom-right corner.
    
    Args:
        maze (List[List[int]]): 2D grid where 0 represents empty spaces and 1 represents walls.
    
    Returns:
        List[Tuple[int, int]]: List of coordinates representing the shortest path.
        If no path exists, returns an empty list.
    """
    if not maze or not maze[0]:
        return []
    
    rows, cols = len(maze), len(maze[0])
    
    # Check start and end points are valid
    if maze[0][0] == 1 or maze[rows-1][cols-1] == 1:
        return []
    
    # Possible moves (including diagonal)
    moves = [
        (0, 1), (0, -1), (1, 0), (-1, 0),  # cardinal directions
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonal moves
    ]
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, 0, 0, [(0, 0)])]  # (distance, row, col, path)
    visited = set()
    
    while pq:
        dist, row, col, path = heapq.heappop(pq)
        
        # Reached the goal
        if row == rows - 1 and col == cols - 1:
            return path
        
        # Skip if already visited
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        # Try all possible moves
        for dx, dy in moves:
            new_row, new_col = row + dx, col + dy
            
            # Check bounds and if the cell is a valid move
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                maze[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                # For diagonal moves, check adjacent cells
                if abs(dx) == 1 and abs(dy) == 1:
                    if (maze[row][new_col] == 1 or maze[new_row][col] == 1):
                        continue
                
                new_path = path + [(new_row, new_col)]
                # Distance is Euclidean (allowing diagonal moves)
                new_dist = dist + ((dx**2 + dy**2)**0.5)
                
                heapq.heappush(pq, (new_dist, new_row, new_col, new_path))
    
    return []  # No path found