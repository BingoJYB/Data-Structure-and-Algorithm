#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (52.02%)
# Likes:    3841
# Dislikes: 85
# Total Accepted:    519.7K
# Total Submissions: 998.9K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def helper(self, nums, result, results):
        if not nums:
            results.append(result)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.helper(nums[:i]+nums[i+1:], result+[nums[i]], results)
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.helper(sorted(nums), [], results)
        return results
    
# @lc code=end

