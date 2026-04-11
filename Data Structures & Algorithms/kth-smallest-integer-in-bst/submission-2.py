# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count =0 
        result = 0
        def dfs(node):
            nonlocal count, result
            if node is None:
                return -1
            dfs(node.left)
            count += 1
            if count == k:
                result = node.val
            dfs(node.right)
        dfs(root)
        return result