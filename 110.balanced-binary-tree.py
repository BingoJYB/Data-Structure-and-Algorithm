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
    memoization = {}
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        isLeftBalanced = self.isBalanced(root.right)
        isRightBalanced = self.isBalanced(root.left)
        left_height = self.getHeight(root.left, 0)
        right_height = self.getHeight(root.right, 0)
        
        return isLeftBalanced and isRightBalanced and True if abs(left_height - right_height) < 2 else False
    
    def getHeight(self, node, height):
        if not node:
            return 0
        
        if node.left in self.memoization.keys():
            left_height = self.memoization[node.left]
        else:
            left_height = self.getHeight(node.left, height)
            self.memoization[node.left] = left_height
            
        if node.right in self.memoization.keys():
            right_height = self.memoization[node.right]
        else:
            right_height = self.getHeight(node.right, height)
            self.memoization[node.right] = right_height
        
        return max(left_height, right_height) + 1
# @lc code=end

