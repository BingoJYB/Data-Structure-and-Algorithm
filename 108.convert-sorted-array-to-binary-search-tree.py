#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (68.49%)
# Likes:    8160
# Dislikes: 411
# Total Accepted:    868.9K
# Total Submissions: 1.3M
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# 
# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        self.buildBST(0, len(nums)-1, nums, root)
        return root
    
    def buildBST(self, lo, hi, nums, node):
        if lo > hi:
            return None
        
        mid = (lo + hi) // 2
        node.val = nums[mid]
        node.left = self.buildBST(lo, mid-1, nums, TreeNode())
        node.right = self.buildBST(mid+1, hi, nums, TreeNode())
        
        return node
# @lc code=end

