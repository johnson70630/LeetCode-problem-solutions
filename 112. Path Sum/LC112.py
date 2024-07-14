from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        need = targetSum - root.val
        if not root.left and not root.right:
            return not need
        return self.hasPathSum(root.left, need) or self.hasPathSum(root.right, need)