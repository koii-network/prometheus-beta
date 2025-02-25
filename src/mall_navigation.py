from typing import Dict, List, Optional
import heapq

class MallMap:
    """
    A class representing a mall map as a weighted graph for navigation.
    
    Attributes:
        graph (Dict[str, Dict[str, int]]): A dictionary representing the mall's store connections.
    """
    
    def __init__(self):
        """
        Initialize an empty mall map graph.
        """
        self.graph: Dict[str, Dict[str, int]] = {}
    
    def add_store(self, store: str) -> None:
        """
        Add a store to the mall map.
        
        Args:
            store (str): The name of the store to add.
        
        Raises:
            ValueError: If the store already exists in the map.
        """
        if store in self.graph:
            raise ValueError(f"Store {store} already exists in the mall map.")
        self.graph[store] = {}
    
    def add_connection(self, store1: str, store2: str, distance: int) -> None:
        """
        Add a connection between two stores with a given distance.
        
        Args:
            store1 (str): First store name.
            store2 (str): Second store name.
            distance (int): Distance between the stores.
        
        Raises:
            ValueError: If either store does not exist in the map.
            ValueError: If distance is negative.
        """
        if store1 not in self.graph:
            raise ValueError(f"Store {store1} does not exist in the mall map.")
        if store2 not in self.graph:
            raise ValueError(f"Store {store2} does not exist in the mall map.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        
        self.graph[store1][store2] = distance
        self.graph[store2][store1] = distance
    
    def find_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        """
        Find the shortest path between two stores using Dijkstra's algorithm.
        
        Args:
            start (str): Starting store name.
            end (str): Destination store name.
        
        Returns:
            Optional[List[str]]: List of stores in the shortest path, or None if no path exists.
        
        Raises:
            ValueError: If either start or end store does not exist in the map.
        """
        # Validate stores exist
        if start not in self.graph:
            raise ValueError(f"Start store {start} does not exist in the mall map.")
        if end not in self.graph:
            raise ValueError(f"End store {end} does not exist in the mall map.")
        
        # If start and end are the same, return single-store path
        if start == end:
            return [start]
        
        # Dijkstra's algorithm
        distances = {store: float('inf') for store in self.graph}
        distances[start] = 0
        previous = {store: None for store in self.graph}
        pq = [(0, start)]
        
        while pq:
            current_distance, current_store = heapq.heappop(pq)
            
            # If we've reached the end store, reconstruct and return the path
            if current_store == end:
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
                
                # If we've found a shorter path, update
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_store
                    heapq.heappush(pq, (distance, neighbor))
        
        # No path found
        return None