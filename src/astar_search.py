import heapq
from typing import List, Tuple, Callable, Any

def astar_search(
    start: Any, 
    is_goal: Callable[[Any], bool], 
    get_neighbors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> List[Any]:
    """
    Implements the A* search algorithm.
    
    Args:
    - start: The starting node
    - is_goal: Function to check if a node is the goal
    - get_neighbors: Function that returns neighboring nodes and their edge costs
    - heuristic: Function that estimates the cost from a node to the goal
    
    Returns:
    - Path from start to goal as a list of nodes, or empty list if no path found
    """
    # Priority queue to store nodes to explore
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Tracking paths and costs
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}
    
    while open_set:
        # Get the node with lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        # Check if goal is reached
        if is_goal(current):
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))
        
        # Explore neighbors
        for neighbor, edge_cost in get_neighbors(current):
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + edge_cost
            
            # If this path to neighbor is better than any previous one
            if (neighbor not in g_score or 
                tentative_g_score < g_score[neighbor]):
                # Update tracking
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                
                # Add to open set if not already present
                if neighbor not in [n[1] for n in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    # No path found
    return []