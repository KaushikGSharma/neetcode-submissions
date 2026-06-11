# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur=root
        if cur!=None:
            print(cur.val)
            left=cur.left
            right=cur.right
            self.invertTree(cur.left)
            self.invertTree(cur.right)
            cur.left=right
            cur.right=left
            
        return root