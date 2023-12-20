class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True


        #build adj_list
        adj_list = defaultdict(list)

        for node in prerequisites:
            u,v = node

            adj_list[v].append(u)

        #build In-degree dictionary

        in_degree = defaultdict(int)

        for node in adj_list:
            in_degree[node]

        for node in adj_list:
            for neighbor in adj_list[node]:
                in_degree[neighbor] +=1
        
        #khans alogrithm

        # for node in in_degree.items():
        #     u,v = node

        #     print(f"{u} indegree {v}")

        queue = deque()

        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        out = []
        while queue:
            u = queue.popleft()
            out.append(u)

            for neighbor in adj_list[u]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        test = set()
        for node in adj_list.items():
            u,v = node
            test.add(u)
            for neighbor in adj_list[u]:
                test.add(neighbor)
        
        # print(list(test))
        
        if len(test) == len(out):
            return True
        return False

        # if len(out) == numCourses:
        #     return True
        # return False
