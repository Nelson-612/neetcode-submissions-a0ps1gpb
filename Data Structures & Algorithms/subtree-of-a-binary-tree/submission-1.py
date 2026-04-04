# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        def isSameTree (tree, sub):
            if not tree and not sub:
                return True
            if not tree or not sub:
                return False
            if tree.val != sub.val:
                return False
            
            return isSameTree(tree.left, sub.left) and isSameTree(tree.right, sub.right)

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)