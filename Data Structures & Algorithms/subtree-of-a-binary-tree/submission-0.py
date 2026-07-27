# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None and subRoot==None:
            return True
        elif root==None:
            return False
        self.is_same=False
        self.postOrder(root,subRoot)
        return self.is_same
            
        
    def postOrder(self, root,subRoot):
        if root==None or self.is_same:
            return

        def checkSum(root1,root2):
            if root1==None and root2==None:
                return True
            elif root1==None or root2==None:
                return False
            if root1.val!=root2.val:
                return False   
            return checkSum(root1.left,root2.left) and checkSum(root1.right,root2.right)
        
        
        if checkSum(root,subRoot):
            self.is_same = True
            return
        
        self.postOrder(root.left,subRoot)
        self.postOrder(root.right,subRoot)