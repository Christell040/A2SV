# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        current = root

        while current is not None:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current

        # Time complexity = o(log(n))

        # " Approach:
        #     so for common anncestor it can either be the root itself or subsequently another parent with 
        #     p and q as its children

        #     so if both p and q are greater than the value of the root they must exist somewhere to the right
        #     same for left

        #     anything else return the current :
        #     other cases can be q is in left subtree and p is in left subtree

        #     *go down
        # " 
        
