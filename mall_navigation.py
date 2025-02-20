import heapq
from typing import Dict, List, Tuple

class MallNavigator:
    def __init__(self, graph: Dict[str, Dict[str, float]]):
        """
        Initialize the mall navigator with a graph representation.
        
        :param graph: A dictionary representing the mall's store connections
                      Key: store name
                      Value: Dictionary of connected stores and their distances
        """
        self.graph = graph
    
    def find_shortest_path(self, start: str, end: str) -> Tuple[List[str], float]:
        """
        Find the shortest path between two stores using Dijkstra's algorithm.
        
        :param start: Starting store name
        :param end: Destination store name
        :return: Tuple of (path, total_distance)
        """
        # Validate input
        if start not in self.graph or end not in self.graph:
            raise ValueError("Start or end store not in mall map")
        
        # Dijkstra's algorithm implementation
        distances = {store: float('inf') for store in self.graph}
        distances[start] = 0
        previous_stores = {store: None for store in self.graph}
        
        pq = [(0, start)]
        
        while pq:
            current_distance, current_store = heapq.heappop(pq)
            
            # If we've reached the destination
            if current_store == end:
                break
            
            # If we've found a longer path, skip
            if current_distance > distances[current_store]:
                continue
            
            # Check all neighboring stores
            for neighbor, weight in self.graph[current_store].items():
                distance = current_distance + weight
                
                # If we've found a shorter path
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_stores[neighbor] = current_store
                    heapq.heappush(pq, (distance, neighbor))
        
        # Reconstruct the path
        path = []
        current = end
        while current:
            path.append(current)
            current = previous_stores[current]
        path.reverse()
        
        # Verify path exists
        if path[0] != start:
            raise ValueError("No path exists between the stores")
        
        return path, distances[end]

# Example usage
if __name__ == "__main__":
    mall_map = {
        "entrance": {"electronics_store": 50, "food_court": 30},
        "electronics_store": {"entrance": 50, "clothing_store": 40},
        "clothing_store": {"electronics_store": 40, "food_court": 20},
        "food_court": {"entrance": 30, "clothing_store": 20}
    }
    
    navigator = MallNavigator(mall_map)
    path, distance = navigator.find_shortest_path("entrance", "clothing_store")
    print(f"Path: {path}")
    print(f"Total Distance: {distance}")