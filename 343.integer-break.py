#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (55.00%)
# Likes:    3188
# Dislikes: 342
# Total Accepted:    205.4K
# Total Submissions: 373.1K
# Testcase Example:  '2'
#
# Given an integer n, break it into the sum of k positive integers, where k >=
# 2, and maximize the product of those integers.
# 
# Return the maximum product you can get.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 58
# 
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4: 
            return n - 1
        
        res = 1
        
        while n > 4:
            n -= 3
            res *= 3
            
        return res * n
# @lc code=end

