import heapq
from typing import List, Tuple, Callable, Any

class Node:
    def __init__(self, state, g_cost=0, h_cost=0, parent=None):
        self.state = state
        self.g_cost = g_cost  # Cost from start node to current node
        self.h_cost = h_cost  # Estimated cost from current node to goal
        self.f_cost = g_cost + h_cost  # Total estimated cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def astar_search(
    start: Any, 
    is_goal: Callable[[Any], bool], 
    get_neighbors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> List[Any]:
    """
    Implement A* search algorithm.
    
    Args:
    - start: Starting state
    - is_goal: Function to check if a state is the goal state
    - get_neighbors: Function to get neighboring states and their costs
    - heuristic: Function to estimate cost to goal
    
    Returns:
    - Path from start to goal as a list of states, or empty list if no path found
    """
    # Initialize start node
    start_node = Node(start, h_cost=heuristic(start))
    
    # Priority queue for open nodes
    open_set = []
    heapq.heappush(open_set, start_node)
    
    # Set to track visited states to avoid revisiting
    closed_set = set()
    
    while open_set:
        # Get node with lowest f_cost
        current_node = heapq.heappop(open_set)
        
        # Check if goal is reached
        if is_goal(current_node.state):
            # Reconstruct path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))
        
        # Mark current state as visited
        closed_set.add(current_node.state)
        
        # Explore neighbors
        for neighbor_state, edge_cost in get_neighbors(current_node.state):
            # Skip if already visited
            if neighbor_state in closed_set:
                continue
            
            # Calculate costs
            g_cost = current_node.g_cost + edge_cost
            h_cost = heuristic(neighbor_state)
            
            # Create neighbor node
            neighbor_node = Node(
                neighbor_state, 
                g_cost=g_cost, 
                h_cost=h_cost, 
                parent=current_node
            )
            
            # Check if neighbor is already in open set with lower cost
            existing_node = next((n for n in open_set if n.state == neighbor_state), None)
            if existing_node and existing_node.f_cost <= neighbor_node.f_cost:
                continue
            
            # Add to open set
            heapq.heappush(open_set, neighbor_node)
    
    # No path found
    return []