#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (56.28%)
# Likes:    5794
# Dislikes: 224
# Total Accepted:    410K
# Total Submissions: 727.5K
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 19
# 
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        state = [0 for _ in range(n+1)]
        state[0], state[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                state[i] += state[j-1] * state[i-j]

        return state[n]
# @lc code=end

