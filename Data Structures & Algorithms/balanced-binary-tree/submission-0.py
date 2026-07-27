# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            self.is_balanced=True
            def depth(root):
                if root==None:
                    return 0
                
                leftH=depth(root.left)
                rightH=depth(root.right)
                if abs(leftH-rightH)>1:
                    self.is_balanced=False
                
                return max(leftH,rightH)+1
            depth(root)
            return self.is_balanced