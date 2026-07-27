# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            self.is_same=True

            def inOrder(root1,root2):
                if root1==None and root2==None:
                    return
                elif root1==None or root2==None:
                    self.is_same=False
                    return
                
                inOrder(root1.left,root2.left)
                if root1.val!=root2.val:
                    self.is_same=False
                inOrder(root1.right,root2.right)

            inOrder(p,q)
            return self.is_same