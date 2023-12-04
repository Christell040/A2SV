class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = {}

        for edge in edges:
            for node in edge:
                degree[node] = degree.get(node,0)+1
        
        for node,out in degree.items():
            if out == len(edges):
                return node
        
        return -1
        
