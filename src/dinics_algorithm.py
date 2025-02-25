from typing import List, Dict
from collections import deque

class Dinic:
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize Dinic's algorithm for maximum flow
        
        :param graph: Adjacency list representation of the graph
                      where graph[u][v] represents capacity from u to v
        """
        self.graph = graph
        self.num_vertices = max(graph.keys()) + 1

    def bfs(self, source: int, sink: int, level: List[int]) -> bool:
        """
        Breadth-first search to build level graph
        
        :param source: Source vertex
        :param sink: Sink vertex
        :param level: List to store level of each vertex
        :return: True if sink is reachable, False otherwise
        """
        # Reset levels
        level[:] = [-1] * self.num_vertices
        level[source] = 0
        
        # Queue for BFS
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v, capacity in self.graph[u].items():
                if level[v] == -1 and capacity > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        return level[sink] != -1

    def dfs(self, u: int, sink: int, flow: int, level: List[int], 
            path_flow: List[int], visited: List[bool]) -> int:
        """
        Depth-first search to find augmenting paths
        
        :param u: Current vertex
        :param sink: Sink vertex
        :param flow: Current flow
        :param level: Level of vertices in level graph
        :param path_flow: Flow on the current path
        :param visited: Visited vertices
        :return: Minimum flow that can be pushed
        """
        if u == sink:
            return flow
        
        visited[u] = True
        
        for v, capacity in self.graph[u].items():
            if not visited[v] and level[v] == level[u] + 1 and capacity > 0:
                curr_flow = min(flow, capacity)
                temp_flow = self.dfs(v, sink, curr_flow, level, path_flow, visited)
                
                if temp_flow > 0:
                    # Update residual graph
                    self.graph[u][v] -= temp_flow
                    
                    # Add reverse edge if not exists
                    if v not in self.graph or u not in self.graph[v]:
                        if v not in self.graph:
                            self.graph[v] = {}
                        self.graph[v][u] = 0
                    
                    self.graph[v][u] += temp_flow
                    return temp_flow
        
        return 0

    def max_flow(self, source: int, sink: int) -> int:
        """
        Calculate maximum flow using Dinic's algorithm
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow from source to sink
        """
        # Validate input
        if source not in self.graph or sink not in self.graph:
            raise ValueError("Source or sink not in graph")
        
        # Auxiliary variables
        max_flow = 0
        level = [-1] * self.num_vertices
        
        # Augment flow while paths exist
        while self.bfs(source, sink, level):
            while True:
                visited = [False] * self.num_vertices
                path_flow = [0]
                
                flow = self.dfs(source, sink, float('inf'), level, path_flow, visited)
                
                if flow == 0:
                    break
                
                max_flow += flow
        
        return max_flow