import heapq
from typing import List, Tuple, Callable, Any

class Node:
    def __init__(self, state, parent=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.g_cost = g_cost  # Cost from start node to current node
        self.h_cost = h_cost  # Estimated cost from current node to goal
        self.f_cost = g_cost + h_cost  # Total estimated cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def astar_search(
    start: Any, 
    goal_test: Callable[[Any], bool], 
    get_successors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> List[Any]:
    """
    Perform A* search algorithm.
    
    Args:
    - start: Starting state
    - goal_test: Function to check if a state is the goal
    - get_successors: Function that returns possible next states and their costs
    - heuristic: Function that estimates cost from a state to the goal
    
    Returns:
    - Path from start to goal as a list of states, or empty list if no path found
    """
    # Initialize open and closed sets
    open_set = []
    closed_set = set()
    
    # Create start node
    start_node = Node(start, g_cost=0, h_cost=heuristic(start))
    heapq.heappush(open_set, start_node)
    
    while open_set:
        # Get node with lowest f_cost
        current_node = heapq.heappop(open_set)
        
        # Check if goal is reached
        if goal_test(current_node.state):
            # Reconstruct path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))
        
        # Add current node to closed set
        closed_set.add(current_node.state)
        
        # Explore successors
        for successor_state, step_cost in get_successors(current_node.state):
            # Skip if successor is already explored
            if successor_state in closed_set:
                continue
            
            # Calculate costs
            g_cost = current_node.g_cost + step_cost
            h_cost = heuristic(successor_state)
            
            # Create successor node
            successor_node = Node(
                successor_state, 
                parent=current_node, 
                g_cost=g_cost, 
                h_cost=h_cost
            )
            
            # Check if successor is already in open set with lower cost
            existing_node = next((n for n in open_set if n.state == successor_state), None)
            if existing_node and existing_node.f_cost <= successor_node.f_cost:
                continue
            
            # Add successor to open set
            heapq.heappush(open_set, successor_node)
    
    # No path found
    return []