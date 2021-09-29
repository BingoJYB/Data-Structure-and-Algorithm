#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (31.36%)
# Likes:    3483
# Dislikes: 886
# Total Accepted:    333.5K
# Total Submissions: 1.1M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions that
# are 4-directionally surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is
# not on the border and it is not connected to an 'O' on the border will be
# flipped to 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# Output: [["X"]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        q = []

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    q.append((i, j))
                    board[i][j] = 'S'

                    while q:
                        pos = q.pop(0)

                        if pos[0] > 0 and board[pos[0]-1][pos[1]] == 'O':
                            q.append((pos[0]-1, pos[1]))
                            board[pos[0]-1][pos[1]] = 'S'

                        if pos[0] < m-1 and board[pos[0]+1][pos[1]] == 'O':
                            q.append((pos[0]+1, pos[1]))
                            board[pos[0]+1][pos[1]] = 'S'

                        if pos[1] > 0 and board[pos[0]][pos[1]-1] == 'O':
                            q.append((pos[0], pos[1]-1))
                            board[pos[0]][pos[1]-1] = 'S'

                        if pos[1] < n-1 and board[pos[0]][pos[1]+1] == 'O':
                            q.append((pos[0], pos[1]+1))
                            board[pos[0]][pos[1]+1] = 'S'

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'S':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
# @lc code=end

