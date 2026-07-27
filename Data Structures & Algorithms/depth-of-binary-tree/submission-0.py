# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depthCheck(root,0)


    def depthCheck(self,root,d):
        if root==None:
            return d
        return max(self.depthCheck(root.left,d),self.depthCheck(root.right,d))+1

        