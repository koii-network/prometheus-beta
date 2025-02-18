from typing import List, Dict

class PushRelabelMaxFlow:
    def __init__(self, graph: Dict[int, Dict[int, int]], source: int, sink: int):
        """
        Initialize the Push-Relabel Maximum Flow algorithm.
        
        :param graph: Adjacency list representation of the graph
        :param source: Source node
        :param sink: Sink node
        """
        self.graph = graph
        self.source = source
        self.sink = sink
        
        # Number of nodes
        self.num_nodes = max(max(graph.keys()), max(max(node for node in graph[key]) for key in graph)) + 1
        
        # Initialize flow network
        self.flow = {u: {v: 0 for v in graph[u]} for u in graph}
        
        # Height (or level) of nodes
        self.height = [0] * self.num_nodes
        self.height[source] = self.num_nodes
        
        # Excess flow at each node
        self.excess_flow = [0] * self.num_nodes
        
        # Initialize preflow by pushing maximum flow from source
        for neighbor, capacity in graph[source].items():
            self.flow[source][neighbor] = capacity
            self.flow[neighbor][source] = -capacity
            self.excess_flow[neighbor] += capacity
            self.excess_flow[source] -= capacity
    
    def push(self, u: int, v: int) -> bool:
        """
        Push excess flow from node u to node v.
        
        :param u: Source node
        :param v: Destination node
        :return: Whether push was successful
        """
        # Calculate the amount to push
        delta = min(self.excess_flow[u], 
                    self.graph[u][v] - self.flow[u][v])
        
        # Update flows
        self.flow[u][v] += delta
        self.flow[v][u] -= delta
        
        # Update excess flows
        self.excess_flow[u] -= delta
        self.excess_flow[v] += delta
        
        return delta > 0
    
    def relabel(self, u: int) -> None:
        """
        Relabel node u by updating its height.
        
        :param u: Node to relabel
        """
        # Find minimum height of admissible neighbors
        min_height = float('inf')
        for v, capacity in self.graph[u].items():
            if self.flow[u][v] < capacity:
                min_height = min(min_height, self.height[v])
        
        # Update height
        self.height[u] = min_height + 1
    
    def max_flow(self) -> int:
        """
        Compute the maximum flow using Push-Relabel algorithm.
        
        :return: Maximum flow value
        """
        # Perform push and relabel operations
        while True:
            # Find an overflowing node
            overflowing_node = None
            for u in range(self.num_nodes):
                if u not in (self.source, self.sink) and self.excess_flow[u] > 0:
                    overflowing_node = u
                    break
            
            # If no overflowing node, break
            if overflowing_node is None:
                break
            
            u = overflowing_node
            pushed = False
            
            # Try to push to neighbors
            for v, capacity in self.graph[u].items():
                if (self.height[u] == self.height[v] + 1 and 
                    self.flow[u][v] < capacity):
                    if self.push(u, v):
                        pushed = True
                        break
            
            # If no push was possible, relabel the node
            if not pushed:
                self.relabel(u)
        
        # Return flow out of the sink
        return sum(self.flow[u][self.sink] for u in self.graph if self.sink in self.graph[u])