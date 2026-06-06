# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         
        res = 0

        # To get Height - a recursive function:
        def dfs(curr):
            #Last Node handling
            if not curr:
                return 0

            #The values of left and right will keep updating every recursion until we get the max and nodes and exhausted 
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal res
            res = max(res, left + right)
            #Returning max height with the root of that recursion round.
            return 1+max(left, right)
        
        dfs(root)
        return res