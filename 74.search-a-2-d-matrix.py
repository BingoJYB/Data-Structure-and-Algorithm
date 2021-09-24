#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (39.95%)
# Likes:    4545
# Dislikes: 218
# Total Accepted:    527.7K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        elif target == matrix[0][0] or target == matrix[m-1][n-1]:
            return True
        else:
            l, r = 0, m - 1

            while l < r:
                mid = (l + r) // 2

                if matrix[mid][-1] < target:
                    l = mid + 1
                elif matrix[mid][-1] > target:
                    r = mid
                else:
                    return True

            candidates = matrix[r]
            l, r = 0, n - 1

            while l < r:
                mid = (l + r) // 2

                if candidates[mid] < target:
                    l = mid + 1
                elif candidates[mid] > target:
                    r = mid
                else:
                    return True

        return False
# @lc code=end

