"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #importance list
        def importance(employees):
            adj_list = {}

            for employee in employees:
                emp_id = employee.id
                importance = employee.importance
                adj_list[emp_id] = importance
            return adj_list

        def sub_list(employees):
            adj_list = {}

            for employee in employees:
                emp_id = employee.id
                subordinates = employee.subordinates
                adj_list[emp_id] = subordinates
            return adj_list

        # a = importance(employees)

        # for u,v in a.items():
        #     print(f"{u} importance {v}")

        # b = sub_list(employees)

        # for x,y in b.items():
        #      print(f"{x} subs {y}")

        importance = importance(employees)
        sub_list = sub_list(employees)
        #dfs code
        stack = [id]
        visited = set()
        total_imp = 0

        while stack:
            current = stack.pop()
            total_imp += importance[current]

            if current in visited:
                continue
            
            visited.add(current)

            stack.extend(neighbor for neighbor in sub_list[current] if neighbor not in visited)
        
        return total_imp



        
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     


