#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (45.69%)
# Likes:    4606
# Dislikes: 109
# Total Accepted:    706.9K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Follow up: Solve it both recursively and iteratively.
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
    def flat_tree(self, node: TreeNode, flatten_tree: List, reverse: bool = False) -> Optional[List]:
        if node is None:
            flatten_tree.append(node)
            return

        flatten_tree.append(node.val)
        
        if not reverse:
            self.flat_tree(node.left, flatten_tree)
            self.flat_tree(node.right, flatten_tree)
        else:
            self.flat_tree(node.right, flatten_tree, reverse=True)
            self.flat_tree(node.left, flatten_tree, reverse=True)

        return flatten_tree

    def isSymmetric(self, root: TreeNode) -> bool:
        flatten_tree = list()
        flatten_tree_reversed = list()

        self.flat_tree(root, flatten_tree)
        self.flat_tree(root, flatten_tree_reversed, reverse=True)

        return flatten_tree == flatten_tree_reversed
# @lc code=end

