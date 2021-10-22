#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (52.20%)
# Likes:    7160
# Dislikes: 348
# Total Accepted:    800.4K
# Total Submissions: 1.5M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
# 
# You must solve this problem without using the library's sort function.
# 
# 
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:
# Input: nums = [0]
# Output: [0]
# Example 4:
# Input: nums = [1]
# Output: [1]
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.
# 
# 
# 
# Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        for color in range(3):
            j = len(nums) - 1

            while i <= j:
                if nums[i] == color:
                    i += 1
                elif nums[j] == color:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1

        return nums
# @lc code=end

