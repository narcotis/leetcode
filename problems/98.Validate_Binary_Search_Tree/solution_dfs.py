# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lower, upper = float("-inf"), float("inf")

        def search(node, lower, upper):
            if not node:
                return True
            elif node.val <= lower or node.val >= upper:
                return False
            else:
                return search(node.left, lower, node.val) and search(node.right, node.val, upper)

        return search(root, lower, upper)