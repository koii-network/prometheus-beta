import heapq
from typing import Dict, List, Tuple, Optional

class MallMap:
    """
    A class representing a mall map as a weighted graph for navigation.
    
    The graph is represented using an adjacency list where each store is a node,
    and connections between stores have weights representing distance or travel time.
    """
    
    def __init__(self):
        """
        Initialize an empty mall map graph.
        
        The graph is stored as a dictionary where:
        - Keys are store names (nodes)
        - Values are dictionaries of connected stores and their distances
        """
        self.graph: Dict[str, Dict[str, float]] = {}
    
    def add_connection(self, store1: str, store2: str, distance: float):
        """
        Add a bidirectional connection between two stores.
        
        Args:
            store1 (str): Name of the first store
            store2 (str): Name of the second store
            distance (float): Distance between the stores
        
        Raises:
            ValueError: If distance is negative
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        
        # Ensure stores exist in the graph
        if store1 not in self.graph:
            self.graph[store1] = {}
        if store2 not in self.graph:
            self.graph[store2] = {}
        
        # Add bidirectional connection
        self.graph[store1][store2] = distance
        self.graph[store2][store1] = distance
    
    def find_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        """
        Find the shortest path between two stores using Dijkstra's algorithm.
        
        Args:
            start (str): Starting store name
            end (str): Destination store name
        
        Returns:
            Optional[List[str]]: List of stores in the shortest path, 
                                 or None if no path exists or a store is not in the graph
        """
        # Validate start store exists
        if start not in self.graph:
            raise KeyError(f"Start store '{start}' not found in mall map")
        
        # If end store doesn't exist, return None 
        if end not in self.graph:
            return None
        
        # If start and end are the same, return direct path
        if start == end:
            return [start]
        
        # Initialize Dijkstra's algorithm
        distances = {store: float('inf') for store in self.graph}
        distances[start] = 0
        previous = {store: None for store in self.graph}
        pq = [(0, start)]
        
        # Find shortest path
        while pq:
            current_distance, current_store = heapq.heappop(pq)
            
            # If we've reached the destination
            if current_store == end:
                # Reconstruct path
                path = []
                while current_store:
                    path.append(current_store)
                    current_store = previous[current_store]
                return list(reversed(path))
            
            # If we've found a longer path, skip
            if current_distance > distances[current_store]:
                continue
            
            # Check neighbors
            for neighbor, weight in self.graph[current_store].items():
                distance = current_distance + weight
                
                # If we've found a shorter path
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_store
                    heapq.heappush(pq, (distance, neighbor))
        
        # No path found
        return None