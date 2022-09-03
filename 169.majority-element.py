#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (63.62%)
# Likes:    11617
# Dislikes: 375
# Total Accepted:    1.4M
# Total Submissions: 2.2M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
# 
# 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(0, len(nums)-1, nums)
    
    def helper(self, lo, hi, nums):
        if lo == hi:
            return nums[lo]
        
        mid = (lo + hi) // 2
        left = self.helper(lo, mid, nums)
        right = self.helper(mid+1, hi, nums)
        
        if left == right:
            return left
        
        left_counter = [1 for num in nums[lo:hi+1] if num == left]
        right_counter = [1 for num in nums[lo:hi+1] if num == right]
        
        return left if sum(left_counter) > sum(right_counter) else right
# @lc code=end

