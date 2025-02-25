from typing import List, Tuple, Callable, Any, Optional
import heapq

class Node:
    """
    Represents a node in the A* search algorithm.
    
    Attributes:
        state: The current state of the node
        g_cost: Cost from the start node to this node
        h_cost: Estimated cost from this node to the goal
        parent: Parent node in the path
    """
    def __init__(self, state: Any, g_cost: float = 0, h_cost: float = 0, parent: Optional['Node'] = None):
        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
    
    @property
    def f_cost(self) -> float:
        """Total estimated cost (g_cost + h_cost)"""
        return self.g_cost + self.h_cost
    
    def __lt__(self, other: 'Node') -> bool:
        """
        Comparison method for heapq to prioritize nodes with lower f_cost
        """
        return self.f_cost < other.f_cost
    
    def __eq__(self, other: object) -> bool:
        """
        Check if two nodes represent the same state
        """
        if not isinstance(other, Node):
            return False
        return self.state == other.state

def astar_search(
    start: Any, 
    is_goal: Callable[[Any], bool], 
    get_neighbors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> Optional[List[Any]]:
    """
    Implement A* search algorithm.
    
    Args:
        start: The starting state
        is_goal: Function to check if a state is the goal state
        get_neighbors: Function that returns neighboring states and their edge costs
        heuristic: Function that estimates the cost to the goal
    
    Returns:
        Optimal path from start to goal, or None if no path exists
    """
    # Validate input functions
    if not callable(is_goal) or not callable(get_neighbors) or not callable(heuristic):
        raise ValueError("is_goal, get_neighbors, and heuristic must be callable")
    
    # Create start node
    start_node = Node(start, g_cost=0, h_cost=heuristic(start))
    
    # Priority queue to store nodes to explore
    open_set = []
    heapq.heappush(open_set, start_node)
    
    # Set to track explored states to avoid revisiting
    closed_set = set()
    
    while open_set:
        # Get the node with lowest f_cost
        current_node = heapq.heappop(open_set)
        
        # Check if current state is goal
        if is_goal(current_node.state):
            # Reconstruct path
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
            neighbor_node = Node(
                neighbor_state, 
                g_cost=g_cost, 
                h_cost=h_cost, 
                parent=current_node
            )
            
            # Check if neighbor is already in open set with a better path
            existing_node = next((n for n in open_set if n.state == neighbor_state), None)
            if existing_node and existing_node.f_cost <= neighbor_node.f_cost:
                continue
            
            # Add or update neighbor in open set
            if existing_node:
                open_set.remove(existing_node)
            heapq.heappush(open_set, neighbor_node)
    
    # No path found
    return None