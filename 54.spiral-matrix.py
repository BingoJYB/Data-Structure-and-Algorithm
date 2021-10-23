#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (39.19%)
# Likes:    5317
# Dislikes: 734
# Total Accepted:    601.3K
# Total Submissions: 1.5M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        while matrix:
            res += matrix.pop(0)

            res += [m.pop(-1) for m in matrix]
            matrix = [m for m in matrix if m]
            
            if matrix:
                res += list(reversed(matrix.pop(-1)))

            if matrix:
                res += [m.pop(0) for m in list(reversed(matrix))]
                matrix = [m for m in matrix if m]

        return res
# @lc code=end

