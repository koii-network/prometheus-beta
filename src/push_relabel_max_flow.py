from typing import List, Dict

class PushRelabelMaxFlow:
    def __init__(self, num_vertices: int):
        """
        Initialize the push-relabel maximum flow algorithm.
        
        :param num_vertices: Number of vertices in the graph
        """
        if num_vertices < 2:
            raise ValueError("Graph must have at least 2 vertices")
        
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.capacity = [[0] * num_vertices for _ in range(num_vertices)]
        self.flow = [[0] * num_vertices for _ in range(num_vertices)]
        self.height = [0] * num_vertices
        self.excess_flow = [0] * num_vertices
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add an edge to the graph with given capacity.
        
        :param u: Source vertex
        :param v: Destination vertex
        :param capacity: Edge capacity
        """
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            raise ValueError(f"Vertex out of range. Must be between 0 and {self.num_vertices - 1}")
        
        if u == v:
            raise ValueError("Cannot add edge from a vertex to itself")
        
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[u][v] = capacity
    
    def push(self, u: int, v: int):
        """
        Push excess flow from vertex u to vertex v.
        
        :param u: Source vertex
        :param v: Destination vertex
        """
        # Amount of flow to push is the minimum of excess flow and remaining capacity
        delta = min(self.excess_flow[u], 
                    self.capacity[u][v] - self.flow[u][v])
        
        self.flow[u][v] += delta
        self.flow[v][u] -= delta
        
        self.excess_flow[u] -= delta
        self.excess_flow[v] += delta
    
    def relabel(self, u: int):
        """
        Relabel vertex u to enable pushing flow.
        
        :param u: Vertex to relabel
        """
        # Set height to minimum possible height of neighboring vertices
        min_height = float('inf')
        for v in self.graph[u]:
            if self.capacity[u][v] - self.flow[u][v] > 0:
                min_height = min(min_height, self.height[v])
        
        # Update height if a valid neighbor is found
        if min_height < float('inf'):
            self.height[u] = min_height + 1
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Validate input vertices
        if source < 0 or source >= self.num_vertices:
            raise ValueError(f"Source vertex {source} out of range")
        
        if sink < 0 or sink >= self.num_vertices:
            raise ValueError(f"Sink vertex {sink} out of range")
        
        if source == sink:
            raise ValueError("Source and sink vertices must be different")
        
        # Initialize preflow
        self.height[source] = self.num_vertices
        
        # Push initial flow from source
        for v in self.graph[source]:
            self.flow[source][v] = self.capacity[source][v]
            self.flow[v][source] = -self.capacity[source][v]
            self.excess_flow[v] = self.capacity[source][v]
            self.excess_flow[source] -= self.capacity[source][v]
        
        # Main push-relabel loop
        while True:
            # Find an overflowing vertex (excluding source and sink)
            overflowing_vertex = None
            for u in range(self.num_vertices):
                if u != source and u != sink and self.excess_flow[u] > 0:
                    overflowing_vertex = u
                    break
            
            # If no overflowing vertex, terminate
            if overflowing_vertex is None:
                break
            
            # Try to push from overflowing vertex
            pushed = False
            for v in self.graph[overflowing_vertex]:
                # Can push if there's remaining capacity and height allows
                if (self.capacity[overflowing_vertex][v] - 
                    self.flow[overflowing_vertex][v] > 0 and 
                    self.height[overflowing_vertex] > self.height[v]):
                    self.push(overflowing_vertex, v)
                    pushed = True
                    break
            
            # If push failed, relabel the vertex
            if not pushed:
                self.relabel(overflowing_vertex)
        
        # Return maximum flow at the sink
        return sum(self.flow[source])