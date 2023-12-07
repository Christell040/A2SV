class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def mat_to_list(mat):
            adj = defaultdict(list)

            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    if mat[row][col] == 1:
                        adj[row].append(col)
            return adj

        graph = mat_to_list(isConnected)

        #recursive dfs

        def dfs(node, adjacency_list, visited):
            visited[node] = True
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                    dfs(neighbor, adjacency_list, visited)

        def counter(adjacency_list):
            num_nodes = len(adjacency_list)
            visited = [False] * num_nodes
            components = 0

            for node in range(num_nodes):
                if not visited[node]:
                    dfs(node, adjacency_list, visited)
                    components += 1

            return components
                
        return counter(graph)
