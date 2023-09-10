class Node():
    def __init__(self,val):
        self.val  = val
        self.next = None

class MinStack(object):

    # def __init__(self):
    #     self.head = Node(None)
    #     self.size = 0
    #     self.min = None
    
    # def empty(self):
    #     return self.size == 0


    # def push(self, val):
    #     if self.size == 0:
    #         self.min = val
    #     new_node = Node(val)
    #     new_node.next = self.head
    #     self.head = new_node
    #     self.size+=1
    #     self.min = min(self.min,val)

    # def pop(self):
    #     if self.empty():
    #         raise Exception("Stack Empty")
    #     self.head = self.head.next
    #     self.size-=1
        

    # def top(self):
    #     return self.head.val
        

    # def getMin(self):
    #     return self.min
    
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Stack to store minimum elements

    def push(self, val) :
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) :
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) :
        if self.stack:
            return self.stack[-1]

    def getMin(self) :
        if self.min_stack:
            return self.min_stack[-1]

    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
