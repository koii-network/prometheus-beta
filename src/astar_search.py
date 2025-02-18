import heapq
from typing import List, Tuple, Callable, Any

def astar_search(
    start: Any, 
    is_goal: Callable[[Any], bool], 
    get_neighbors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> List[Any]:
    """
    Implement A* search algorithm.
    
    Args:
    - start: Starting node
    - is_goal: Function to check if a node is the goal
    - get_neighbors: Function that returns neighboring nodes and their costs
    - heuristic: Function that estimates the cost to the goal
    
    Returns:
    - Path from start to goal as a list of nodes, or empty list if no path found
    """
    # Priority queue to store nodes to explore
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Track the best path to each node
    came_from = {}
    
    # Track actual cost to reach each node
    g_score = {start: 0}
    
    # Track estimated total cost through each node
    f_score = {start: heuristic(start)}
    
    while open_set:
        # Get node with lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        # Check if we've reached the goal
        if is_goal(current):
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))
        
        # Explore neighbors
        for neighbor, cost in get_neighbors(current):
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + cost
            
            # If this path to neighbor is better than any previous one
            if (neighbor not in g_score or 
                tentative_g_score < g_score[neighbor]):
                
                # Update tracking information
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                
                # Add to open set if not already present
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    # No path found
    return []