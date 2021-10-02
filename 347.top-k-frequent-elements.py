#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.50%)
# Likes:    6121
# Dislikes: 301
# Total Accepted:    682.7K
# Total Submissions: 1.1M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        
        for num in nums:
            count[num] = count.setdefault(num, 0) + 1

        return heapq.nlargest(k, count, count.get)
# @lc code=end

