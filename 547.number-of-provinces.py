#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# https://leetcode.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (63.05%)
# Likes:    6025
# Dislikes: 259
# Total Accepted:    524.5K
# Total Submissions: 831.7K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.
# 
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
# 
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# i^th city and the j^th city are directly connected, and isConnected[i][j] = 0
# otherwise.
# 
# Return the total number of provinces.
# 
# 
# Example 1:
# 
# 
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# 
# 
#

# @lc code=start
from re import T


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        
        if len(isConnected) == 0:
            return res
        
        row = len(isConnected)
        col = len(isConnected[0])
        visited = [False] * row
        
        for i in range(row):
            res += self.helper(i, row, col, visited, isConnected)
                    
        return res
    
    def helper(self, curr_row, row, col, visited, isConnected):
        if visited[curr_row] is True:
            return 0
        
        visited[curr_row] = True
        
        for j in range(col):
            if isConnected[curr_row][j] == 1 and visited[j] is False:
                self.helper(j, row, col, visited, isConnected)
                
        return 1
# @lc code=end

