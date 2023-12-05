from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def edge_list_to_adjacency_list(edges):
            adjacency_list = {}

            for edge in edges:
                u, v = edge
                adjacency_list.setdefault(u, []).append(v)
                adjacency_list.setdefault(v, []).append(u)
            
            # Make sure all vertices are included in the dictionary
            for i in range(n):
                adjacency_list.setdefault(i, [])

            return adjacency_list               
        
        def iterative_dfs(graph, source, destination):
            stack = [source]
            visited = set()

            path = []

            while stack:
                current = stack.pop()

                if current in visited:
                    continue
                
                path.append(current)
                visited.add(current)

                stack.extend([neighbor for neighbor in graph[current] if neighbor not in visited])
            
            if destination in path:
                return True
            return False

        graph = edge_list_to_adjacency_list(edges)
    
        return iterative_dfs(graph, source, destination)


