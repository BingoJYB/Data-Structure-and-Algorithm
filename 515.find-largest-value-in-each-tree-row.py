#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (64.60%)
# Likes:    2287
# Dislikes: 90
# Total Accepted:    206.3K
# Total Submissions: 319.3K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return an array of the largest value in each
# row of the tree (0-indexed).
# 
# 
# Example 1:
# 
# 
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3]
# Output: [1,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [0, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
import math


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q1 = [root]
        q2 = []
        
        if root is None:
            return res
        
        while q1 or q2:
            max_val = -math.inf
            
            if q1:
                while q1:
                    curr_node = q1.pop(0)
                    max_val = curr_node.val if curr_node.val > max_val else max_val
                    
                    if curr_node.left is not None:
                        q2.append(curr_node.left)
                        
                    if curr_node.right is not None:
                        q2.append(curr_node.right)
            elif q2:
                while q2:
                    curr_node = q2.pop(0)
                    max_val = curr_node.val if curr_node.val > max_val else max_val
                
                    if curr_node.left is not None:
                        q1.append(curr_node.left)
                
                    if curr_node.right is not None:
                        q1.append(curr_node.right)
                        
            res.append(max_val)
            
        return res
        
# @lc code=end

