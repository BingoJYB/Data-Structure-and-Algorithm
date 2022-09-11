#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (66.09%)
# Likes:    2482
# Dislikes: 232
# Total Accepted:    190K
# Total Submissions: 287.2K
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
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
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        temp_q = []
        res = []
        
        while q:
            node = q.pop(0)
            res.append(node.val)
            
            if node.left:
                temp_q.append(node.left)
                
            if node.right:
                temp_q.append(node.right)
                
            if not q and temp_q:
                q = temp_q[:]
                temp_q = []
                res = []
                
        return res[0]
# @lc code=end

