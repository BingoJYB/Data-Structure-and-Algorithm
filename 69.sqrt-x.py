#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (35.98%)
# Likes:    2700
# Dislikes: 2734
# Total Accepted:    852.5K
# Total Submissions: 2.4M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
# 
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
# 
# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.
# 
# 
# Example 1:
# 
# 
# Input: x = 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
# 
# 
# Constraints:
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        for i in range(1, x):
            temp = i ** 2

            if temp == x:
                return i
            elif temp > x:
                return i - 1

        return x - 1
# @lc code=end

