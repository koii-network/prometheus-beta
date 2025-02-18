from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize Dinic's max flow algorithm with a graph representation.
        
        :param graph: A dictionary representing the graph where keys are nodes 
                      and values are dictionaries of adjacent nodes and their capacities
        """
        self.graph = graph
        self.nodes = set(graph.keys())
        
    def bfs(self, source: int, sink: int, level: List[int]) -> bool:
        """
        Breadth-first search to construct level graph and check if sink is reachable.
        
        :param source: Source node
        :param sink: Sink node
        :param level: List to store level of each node
        :return: Boolean indicating if sink is reachable
        """
        # Reset level array
        level[:] = [-1] * len(level)
        level[source] = 0
        
        # Queue for BFS
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            for neighbor, capacity in self.graph[current].items():
                if level[neighbor] == -1 and capacity > 0:
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)
        
        return level[sink] != -1
    
    def dfs(self, node: int, sink: int, flow: int, level: List[int], 
            visited: List[bool], graph_flow: Dict[int, Dict[int, int]]) -> int:
        """
        Depth-first search to find augmenting paths in the level graph.
        
        :param node: Current node
        :param sink: Sink node
        :param flow: Current flow
        :param level: Level of each node
        :param visited: Visited nodes tracker
        :param graph_flow: Graph tracking current flow
        :return: Augmented flow
        """
        if node == sink:
            return flow
        
        visited[node] = True
        
        for neighbor, capacity in self.graph[node].items():
            residual_capacity = capacity - graph_flow[node].get(neighbor, 0)
            
            if (not visited[neighbor] and 
                level[neighbor] == level[node] + 1 and 
                residual_capacity > 0):
                
                curr_flow = min(flow, residual_capacity)
                temp_flow = self.dfs(neighbor, sink, curr_flow, level, visited, graph_flow)
                
                if temp_flow > 0:
                    graph_flow[node][neighbor] = graph_flow[node].get(neighbor, 0) + temp_flow
                    graph_flow[neighbor][node] = graph_flow[neighbor].get(node, 0) - temp_flow
                    return temp_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink using Dinic's algorithm.
        
        :param source: Source node
        :param sink: Sink node
        :return: Maximum flow value
        """
        # Validate input nodes
        if source not in self.nodes or sink not in self.nodes:
            raise ValueError("Source or sink node not in graph")
        
        if source == sink:
            return 0
        
        # Initialize graph for flow tracking
        graph_flow = {node: {} for node in self.nodes}
        
        # Nodes tracking
        node_list = list(self.nodes)
        node_indices = {node: idx for idx, node in enumerate(node_list)}
        
        max_flow = 0
        level = [-1] * len(node_list)
        
        # Dinic's algorithm
        while self.bfs(source, sink, level):
            while True:
                visited = [False] * len(node_list)
                flow = self.dfs(source, sink, float('inf'), level, visited, graph_flow)
                
                if flow == 0:
                    break
                
                max_flow += flow
        
        return max_flow