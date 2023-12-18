# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_middle(head):
            if not head:
                return None

            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(left, right):
            dummy = ListNode()
            current = dummy

            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next

                current = current.next

            # If there are remaining nodes in left or right
            if left:
                current.next = left
            elif right:
                current.next = right

            return dummy.next

        if not head or not head.next:
            return head

        middle = get_middle(head)
        second_half = middle.next
        middle.next = None  

        
        left = self.sortList(head)
        right = self.sortList(second_half)

        return merge(left, right)
