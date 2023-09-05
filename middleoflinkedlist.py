# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head): 
        #Bruteforce approach  - passed 50%    
        # self.size = 0
        # current = head
        # while current:
        #     self.size+=1
        #     current = current.next
        
        # if self.size % 2 == 1:
        #     middle = (self.size // 2) 
        #     currentz = head
        #     index = 0
        #     while currentz and index != middle:
        #         index+=1
        #         currentz = currentz.next
        #     return currentz

        # if self.size % 2 == 0:
        #     middle = (self.size // 2) 
        #     currenta = head
        #     index = 0
        #     while currenta and index != middle:
        #         index+=1
        #         currenta = currenta.next
        #     return currenta


        "Tortoise and hare approach"
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

        "Beats 77.8 o(n)"







        
