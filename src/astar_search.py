from typing import List, Tuple, Callable, Any, Optional
import heapq
import math

class Node:
    def __init__(self, state: Any, g_cost: float, h_cost: float, parent: Optional['Node'] = None):
        """
        Initialize a node for A* search algorithm.
        
        Args:
            state: The current state of the node
            g_cost: Cost from the start node to the current node
            h_cost: Estimated cost from the current node to the goal
            parent: Parent node in the search path
        """
        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent
    
    def __lt__(self, other):
        """
        Allow comparison between nodes for priority queue.
        
        Args:
            other: Another node to compare with
        
        Returns:
            bool: True if this node's f_cost is less than the other's
        """
        return self.f_cost < other.f_cost

def astar_search(
    start: Any, 
    is_goal: Callable[[Any], bool], 
    get_neighbors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> Optional[List[Any]]:
    """
    Perform A* search algorithm.
    
    Args:
        start: The starting state
        is_goal: Function to check if a state is the goal state
        get_neighbors: Function to get neighboring states and their costs
        heuristic: Function to estimate cost to goal
    
    Returns:
        Optional list of states representing the path from start to goal, 
        or None if no path is found
    """
    # Initialize the start node
    start_node = Node(start, 0, heuristic(start))
    
    # Priority queue to store nodes to explore
    open_set = []
    heapq.heappush(open_set, start_node)
    
    # Set to keep track of explored states
    closed_set = set()
    
    while open_set:
        # Get the node with the lowest f_cost
        current_node = heapq.heappop(open_set)
        
        # Check if we've reached the goal
        if is_goal(current_node.state):
            # Reconstruct the path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))
        
        # Mark current state as explored
        closed_set.add(current_node.state)
        
        # Explore neighbors
        for neighbor_state, edge_cost in get_neighbors(current_node.state):
            # Skip already explored states
            if neighbor_state in closed_set:
                continue
            
            # Calculate costs
            g_cost = current_node.g_cost + edge_cost
            h_cost = heuristic(neighbor_state)
            
            # Create neighbor node
            neighbor_node = Node(neighbor_state, g_cost, h_cost, current_node)
            
            # Check if neighbor is already in open set with a better path
            existing_node = next((n for n in open_set if n.state == neighbor_state and n.f_cost <= neighbor_node.f_cost), None)
            
            if existing_node is None:
                heapq.heappush(open_set, neighbor_node)
    
    # No path found
    return None