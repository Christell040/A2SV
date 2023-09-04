# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        arr=[]
        current= head
        while current:
            arr.append(current.val)
            current=current.next
        
        arr[left-1:right]=arr[left-1:right][::-1]
        x=0
        print(arr)
        current=head

        while current:
            current.val=arr[x]
            x+=1
            current=current.next


        return head
            