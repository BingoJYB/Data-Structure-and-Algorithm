#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/
#
# algorithms
# Medium (74.83%)
# Likes:    1125
# Dislikes: 284
# Total Accepted:    36K
# Total Submissions: 48K
# Testcase Example:  '14'
#
# In an infinite binary tree where every node has two children, the nodes are
# labelled in row order.
# 
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is
# left to right, while in the even numbered rows (second, fourth, sixth,...),
# the labelling is right to left.
# 
# 
# 
# Given the label of a node in this tree, return the labels in the path from
# the root of the tree to the node with that label.
# 
# 
# Example 1:
# 
# 
# Input: label = 14
# Output: [1,3,4,14]
# 
# 
# Example 2:
# 
# 
# Input: label = 26
# Output: [1,2,6,10,26]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= label <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 0
        test_num = 1
        res = [label]
        
        while test_num <= label:
            level += 1
            test_num *= 2
            
        for i in range(level-1, 0, -1):
            res.append(2 ** i - 1 + 2 ** (i - 1) - res[-1] // 2)
            
        return res[::-1]
# @lc code=end

