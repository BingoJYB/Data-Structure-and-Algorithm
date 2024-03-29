#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (69.77%)
# Likes:    7838
# Dislikes: 155
# Total Accepted:    955K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def helper(self, nums, result, results):
        if not nums:
            return results.append(result)

        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:], result+[nums[i]], results)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.helper(nums, [], results)
        return results
        
# @lc code=end

