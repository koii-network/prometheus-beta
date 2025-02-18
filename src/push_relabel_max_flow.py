from typing import List, Dict, Tuple

class PushRelabelMaxFlow:
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize the push-relabel maximum flow algorithm.
        
        :param graph: Adjacency list representation of the graph 
                      where graph[u][v] represents capacity from u to v
        """
        self.graph = graph
        self.num_vertices = len(graph)
        
        # Initialize flow network
        self.flow = {u: {v: 0 for v in graph[u]} for u in graph}
        
        # Initialize height (preflow) and excess flow for each vertex
        self.height = {v: 0 for v in graph}
        self.excess = {v: 0 for v in graph}
    
    def initialize_preflow(self, source: int):
        """
        Initialize preflow by setting height of source to number of vertices
        and saturating outgoing edges from source.
        
        :param source: Source vertex
        """
        self.height[source] = self.num_vertices
        
        for neighbor, capacity in self.graph[source].items():
            # Push maximum possible flow to neighbors of source
            self.flow[source][neighbor] = capacity
            self.flow[neighbor][source] = -capacity
            
            # Update excess flow
            self.excess[neighbor] = capacity
            self.excess[source] -= capacity
    
    def push(self, u: int, v: int) -> bool:
        """
        Push excess flow from vertex u to vertex v.
        
        :param u: Source vertex with excess flow
        :param v: Destination vertex
        :return: True if push was successful, False otherwise
        """
        # Calculate the amount that can be pushed
        push_amount = min(
            self.excess[u], 
            self.graph[u][v] - self.flow[u][v]
        )
        
        # Only push if there's capacity and height condition is met
        if push_amount > 0 and self.height[u] > self.height[v]:
            self.flow[u][v] += push_amount
            self.flow[v][u] -= push_amount
            
            self.excess[u] -= push_amount
            self.excess[v] += push_amount
            
            return True
        
        return False
    
    def relabel(self, u: int):
        """
        Relabel vertex u by increasing its height.
        
        :param u: Vertex to relabel
        """
        # Find the minimum height of adjacent vertices with residual capacity
        min_height = float('inf')
        for v, capacity in self.graph[u].items():
            if capacity > self.flow[u][v]:
                min_height = min(min_height, self.height[v])
        
        # Increase height of u
        if min_height < float('inf'):
            self.height[u] = min_height + 1
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute maximum flow using push-relabel algorithm.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Validate source and sink
        if source not in self.graph or sink not in self.graph:
            raise ValueError("Source or sink not in graph")
        
        if source == sink:
            return 0
        
        # Initialize preflow
        self.initialize_preflow(source)
        
        # Create list of active vertices (with excess flow)
        active_vertices = [
            v for v in self.graph 
            if v != source and v != sink and self.excess[v] > 0
        ]
        
        while active_vertices:
            u = active_vertices.pop(0)
            
            # Try pushing to all neighbors
            for v in self.graph[u]:
                if v == u:
                    continue
                
                # Try to push flow
                if self.push(u, v):
                    # If v now has excess and is not source/sink, add to active list
                    if v != source and v != sink and self.excess[v] > 0:
                        active_vertices.append(v)
            
            # If still has excess, relabel
            if self.excess[u] > 0:
                self.relabel(u)
                active_vertices.append(u)
        
        # Return flow to sink
        return sum(self.flow[source].values())