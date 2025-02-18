import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Implement Dijkstra's algorithm to find shortest paths from a start node.

    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph
        start (str): Starting node for path calculation

    Returns:
        Tuple containing:
        - Dict of shortest distances from start node to all other nodes
        - Dict of previous nodes in the shortest path
    """
    # Validate input
    if not graph or start not in graph:
        raise ValueError("Invalid graph or start node")

    # Initialize distances and previous nodes for ALL nodes
    all_nodes = set(graph.keys()).union(
        node for nodes in graph.values() for node in nodes.keys()
    )
    distances = {node: float('inf') for node in all_nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in all_nodes}

    # Priority queue to store nodes to visit
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue

        # Only process neighbors if the current node is in the graph
        if current_node in graph:
            # Check neighbors
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight

                # If new path is shorter, update distance and previous node
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes: Dict[str, str], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path between start and end nodes.

    Args:
        previous_nodes (Dict[str, str]): Dictionary of previous nodes
        start (str): Starting node
        end (str): Ending node

    Returns:
        List of nodes in the shortest path from start to end
    """
    path = []
    current = end

    # Trace back from end to start
    while current is not None:
        path.append(current)
        current = previous_nodes.get(current)

    # If path is not complete, return empty list
    if not path or path[-1] != start:
        return []

    # Reverse to get path from start to end
    return list(reversed(path))