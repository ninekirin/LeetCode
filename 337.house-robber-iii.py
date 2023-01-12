#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rob_sub(root))

    def rob_sub(self, root):
        if not root:
            return (0, 0)
        left = self.rob_sub(root.left)
        right = self.rob_sub(root.right)
        return (max(left) + max(right), root.val + left[0] + right[0])
# @lc code=end

