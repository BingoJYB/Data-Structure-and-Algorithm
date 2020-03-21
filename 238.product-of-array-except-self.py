#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (58.71%)
# Likes:    3793
# Dislikes: 322
# Total Accepted:    403K
# Total Submissions: 684.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        R = 1

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        for i in reversed(range(len(nums))):
            result[i] = result[i] * R
            R *= nums[i]

        return result
# @lc code=end

