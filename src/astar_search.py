import heapq
from typing import List, Tuple, Callable, Any, Optional

class Node:
    """
    Represents a node in the A* search algorithm.
    
    Attributes:
        state: Current state of the node
        g_cost: Cost from start node to current node
        h_cost: Estimated cost from current node to goal
        parent: Parent node in the path
    """
    def __init__(self, state: Any, g_cost: float, h_cost: float, parent: Optional['Node'] = None):
        """
        Initialize a node for A* search.
        
        Args:
            state: The current state
            g_cost: Cost from start node to current node
            h_cost: Estimated cost from current node to goal
            parent: Parent node in the path (optional)
        """
        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
    
    @property
    def f_cost(self) -> float:
        """
        Calculate total estimated cost (f = g + h).
        
        Returns:
            Total estimated cost
        """
        return self.g_cost + self.h_cost
    
    def __lt__(self, other: 'Node') -> bool:
        """
        Compare nodes based on f_cost for priority queue.
        
        Args:
            other: Another node to compare
        
        Returns:
            True if this node has lower f_cost
        """
        return self.f_cost < other.f_cost

def astar_search(
    start: Any, 
    is_goal: Callable[[Any], bool], 
    get_neighbors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> Optional[List[Any]]:
    """
    Implement A* search algorithm.
    
    Args:
        start: Starting state
        is_goal: Function to check if a state is the goal
        get_neighbors: Function to get neighboring states and their costs
        heuristic: Function to estimate cost to goal
    
    Returns:
        Optimal path from start to goal, or None if no path exists
    """
    # Priority queue to store nodes to explore
    open_set = []
    # Track explored states to avoid revisiting
    closed_set = set()
    
    # Create initial node
    start_node = Node(start, 0, heuristic(start))
    heapq.heappush(open_set, start_node)
    
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
        
        # Mark current state as explored
        closed_set.add(current_node.state)
        
        # Explore neighbors
        for neighbor_state, step_cost in get_neighbors(current_node.state):
            # Skip already explored states
            if neighbor_state in closed_set:
                continue
            
            # Calculate costs
            g_cost = current_node.g_cost + step_cost
            h_cost = heuristic(neighbor_state)
            
            # Create neighbor node
            neighbor_node = Node(
                neighbor_state, 
                g_cost, 
                h_cost, 
                parent=current_node
            )
            
            # Check if neighbor is already in open set with lower cost
            existing_node = next(
                (n for n in open_set if n.state == neighbor_state), 
                None
            )
            
            if existing_node:
                # Replace if new path is more optimal
                if g_cost < existing_node.g_cost:
                    open_set.remove(existing_node)
                    heapq.heappush(open_set, neighbor_node)
            else:
                # Add new neighbor to explore
                heapq.heappush(open_set, neighbor_node)
    
    # No path found
    return None