#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (47.84%)
# Likes:    7267
# Dislikes: 379
# Total Accepted:    918.9K
# Total Submissions: 1.9M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
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
    res = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.getHeight(root)
        return self.res
    
    def getHeight(self, node):
        if not node:
            return 0
        
        right_height = self.getHeight(node.right)
        left_height = self.getHeight(node.left)
        
        if self.res:
            self.res = abs(left_height - right_height) < 2
        
        return max(left_height, right_height) + 1
# @lc code=end

