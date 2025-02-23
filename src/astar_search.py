import heapq
from typing import List, Tuple, Callable, Any, Optional

class Node:
    """Represents a node in the A* search algorithm."""
    def __init__(self, state: Any, g_cost: float, h_cost: float, parent: Optional['Node'] = None):
        """
        Initialize a node for A* search.
        
        :param state: The current state
        :param g_cost: Cost from the start node to the current node
        :param h_cost: Estimated cost from the current node to the goal
        :param parent: Parent node in the search path
        """
        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other: 'Node') -> bool:
        """
        Allow comparison of nodes for the priority queue.
        
        :param other: Another node to compare
        :return: True if this node has lower f_cost
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
    
    :param start: Starting state
    :param is_goal: Function to check if a state is the goal
    :param get_neighbors: Function to get neighboring states and their costs
    :param heuristic: Heuristic function to estimate cost to goal
    :return: Path from start to goal, or None if no path exists
    """
    # Handle invalid inputs
    if start is None or not callable(is_goal) or not callable(get_neighbors) or not callable(heuristic):
        raise ValueError("Invalid input parameters")

    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Create the start node
    start_node = Node(start, 0, heuristic(start))
    heapq.heappush(open_set, start_node)

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

        # Add current node to closed set
        closed_set.add(current_node.state)

        # Explore neighbors
        for neighbor_state, step_cost in get_neighbors(current_node.state):
            # Skip already explored states
            if neighbor_state in closed_set:
                continue

            # Calculate costs
            g_cost = current_node.g_cost + step_cost
            h_cost = heuristic(neighbor_state)
            neighbor_node = Node(neighbor_state, g_cost, h_cost, current_node)

            # Check if neighbor is already in open set with a better path
            existing_node = next((n for n in open_set if n.state == neighbor_state), None)
            if existing_node and existing_node.f_cost <= neighbor_node.f_cost:
                continue

            # Add or update the neighbor in the open set
            if existing_node:
                open_set.remove(existing_node)
            heapq.heappush(open_set, neighbor_node)

    # No path found
    return None