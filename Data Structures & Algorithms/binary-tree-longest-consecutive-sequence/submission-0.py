# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, parent_val, length):
            if not node:
                return length

            if node.val == parent_val + 1:
                length += 1
            else:
                length = 1

            res = max(length, dfs(node.left, node.val, length), dfs(node.right, node.val, length))

            return res

        return dfs(root, root.val -1, 0)