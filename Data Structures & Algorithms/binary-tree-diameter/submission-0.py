# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxH=0

        def checkDiameterWithCurNode(root):
            if root==None:
                return 0
            leftMax=checkDiameterWithCurNode(root.left)
            rightMax=checkDiameterWithCurNode(root.right)
            sum=leftMax+rightMax
            self.maxH=max(sum,self.maxH)
            return max(leftMax,rightMax) + 1

        checkDiameterWithCurNode(root)
        return self.maxH