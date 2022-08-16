#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (58.13%)
# Likes:    8192
# Dislikes: 473
# Total Accepted:    800.6K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root = [1,null,3]
# Output: [1,3]
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
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            queue = [root]
        else:
            return []
        temp_q = []
        res = []

        while queue:
            node = queue.pop(0)

            if node.left:
                temp_q.append(node.left)
            
            if node.right:
                temp_q.append(node.right)

            if not queue:
                res.append(node.val)

                if temp_q:
                    queue = temp_q[:]
                    temp_q = []

        return res
# @lc code=end

