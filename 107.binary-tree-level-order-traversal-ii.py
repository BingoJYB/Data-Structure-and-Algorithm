#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Medium (56.85%)
# Likes:    2551
# Dislikes: 260
# Total Accepted:    450.5K
# Total Submissions: 790.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the bottom-up level order traversal
# of its nodes' values. (i.e., from left to right, level by level from leaf to
# root).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        q = [root]
        res = []
        node_vals = []
        temp_q = []

        while q:
            node = q.pop(0)
            node_vals.append(node.val)

            if node.left:
                temp_q.append(node.left)

            if node.right:
                temp_q.append(node.right)

            if not q and node_vals:
                res.insert(0, node_vals[:])
                q = temp_q[:]
                node_vals = []
                temp_q = []

        return res
# @lc code=end

