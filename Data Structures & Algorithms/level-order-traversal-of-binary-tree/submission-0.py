# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth_dict=defaultdict(list)
        depth=1

        def depthTraversal(cur: Optional[TreeNode], depth ):
           
            if cur:
                # print(cur.val)
                depth_dict[depth].append(cur.val)
                depthTraversal(cur.left,depth+1)
                depthTraversal(cur.right,depth+1)

        depthTraversal(root,depth)
        result=[]
        for key,val in depth_dict.items():
            result.append(val)
        return result
        