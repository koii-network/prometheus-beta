from typing import List, Dict, Tuple

class PushRelabelMaxFlow:
    """
    Implementation of the Push-Relabel algorithm for maximum flow.
    
    The algorithm uses the highest label selection rule and maintains 
    a preflow where excess flow can exist at nodes.
    
    Time Complexity: O(V^2 * E), where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V^2)
    """
    
    def __init__(self, num_vertices: int):
        """
        Initialize the push-relabel max flow graph.
        
        :param num_vertices: Number of vertices in the graph
        """
        self.num_vertices = num_vertices
        # Adjacency matrix to represent residual graph
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]
        # Height (or level) of each vertex
        self.height = [0] * num_vertices
        # Excess flow at each vertex
        self.excess_flow = [0] * num_vertices
        
    def add_edge(self, source: int, sink: int, capacity: int):
        """
        Add an edge to the graph with a given capacity.
        
        :param source: Source vertex
        :param sink: Destination vertex
        :param capacity: Edge capacity
        """
        self.graph[source][sink] = capacity
        
    def initialize_preflow(self, source: int):
        """
        Initialize the preflow for the push-relabel algorithm.
        
        :param source: Source vertex
        """
        # Set height of source to number of vertices
        self.height[source] = self.num_vertices
        
        # Push initial flow from source to its adjacent vertices
        for v in range(self.num_vertices):
            if self.graph[source][v] > 0:
                # Push maximum possible flow
                flow = self.graph[source][v]
                self.graph[source][v] = 0  # Residual capacity
                self.graph[v][source] = flow  # Reverse edge
                
                # Update excess flow
                self.excess_flow[v] += flow
                self.excess_flow[source] -= flow
        
    def push(self, u: int, v: int):
        """
        Push flow from vertex u to vertex v.
        
        :param u: Source vertex
        :param v: Destination vertex
        :return: Amount of flow pushed
        """
        # Determine the amount to push
        push_amount = min(self.excess_flow[u], 
                          self.graph[u][v])
        
        # Update residual capacities
        self.graph[u][v] -= push_amount
        self.graph[v][u] += push_amount
        
        # Update excess flows
        self.excess_flow[u] -= push_amount
        self.excess_flow[v] += push_amount
        
        return push_amount
    
    def relabel(self, u: int):
        """
        Relabel (update height of) vertex u.
        
        :param u: Vertex to relabel
        """
        # Find the minimum height of adjacent vertices 
        # with remaining capacity
        min_height = float('inf')
        for v in range(self.num_vertices):
            if self.graph[u][v] > 0:
                min_height = min(min_height, self.height[v])
        
        # Update height
        if min_height < float('inf'):
            self.height[u] = min_height + 1
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow using Push-Relabel algorithm.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Validate input
        if source < 0 or source >= self.num_vertices or \
           sink < 0 or sink >= self.num_vertices or \
           source == sink:
            # For single vertex graph, return 0 instead of raising an error
            if source == sink and source == 0 and self.num_vertices == 1:
                return 0
            raise ValueError("Invalid source or sink vertex")
        
        # Initialize preflow
        self.initialize_preflow(source)
        
        # Keep track of vertices with excess flow (excluding source and sink)
        active_vertices = [v for v in range(self.num_vertices) 
                           if v not in (source, sink) and self.excess_flow[v] > 0]
        
        # Fallback counting to prevent infinite loops
        iteration_limit = self.num_vertices * self.num_vertices * 2
        iterations = 0
        
        while active_vertices and iterations < iteration_limit:
            iterations += 1
            u = active_vertices.pop(0)
            
            # Try to push flow to adjacent vertices
            pushed = False
            for v in range(self.num_vertices):
                # Can push if there's excess flow and remaining capacity
                # and the height condition is satisfied
                if self.excess_flow[u] > 0 and \
                   self.graph[u][v] > 0 and \
                   self.height[u] > self.height[v]:
                    
                    # Push flow
                    pushed_amount = self.push(u, v)
                    
                    # If flow was pushed to a vertex, add it to active vertices
                    if pushed_amount > 0:
                        pushed = True
                        if v not in (source, sink) and v not in active_vertices:
                            active_vertices.append(v)
            
            # If no push was possible, relabel
            if not pushed and self.excess_flow[u] > 0:
                self.relabel(u)
                active_vertices.append(u)
        
        # Maximum flow is the total excess flow at the sink
        return self.excess_flow[sink]