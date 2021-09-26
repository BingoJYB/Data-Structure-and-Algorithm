#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (60.22%)
# Likes:    2953
# Dislikes: 97
# Total Accepted:    414.2K
# Total Submissions: 684.8K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of the range [1, n].
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= k <= n
# 
# 
#

# @lc code=start
class Solution:
    def combineUtil(self, s, n, k, can, arrs):
        if k == 0:
            arrs.append(can[:])
            return

        for i in range(s+1, n+1):
            can.append(i)
            self.combineUtil(i, n, k-1, can, arrs)
            can.pop()
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.combineUtil(0, n, k, [], res)
        return res
# @lc code=end

