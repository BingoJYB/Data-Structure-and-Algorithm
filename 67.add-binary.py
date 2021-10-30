#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (48.81%)
# Likes:    3561
# Dislikes: 420
# Total Accepted:    694.6K
# Total Submissions: 1.4M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
# 
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            
            if b:
                carry += int(b.pop())

            result = str(carry % 2) + result
            carry //= 2

        return result
# @lc code=end

