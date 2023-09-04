# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        dummy_small = ListNode(0)
        dummy_large = ListNode(0)
        small_ptr = dummy_small
        large_ptr = dummy_large
        current = head

        while current:
            if current.val >= x:
                large_ptr.next = current
                large_ptr = large_ptr.next
            else:
                small_ptr.next = current
                small_ptr = small_ptr.next
            current = current.next

        large_ptr.next = None
        small_ptr.next = dummy_large.next
        return dummy_small.next
