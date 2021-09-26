#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (38.35%)
# Likes:    6908
# Dislikes: 269
# Total Accepted:    758.7K
# Total Submissions: 2M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
class Solution:
    def existUtil(self, board, word, i, j, c):
        if c == len(word):
            return True

        if (
            i < 0 
            or i == len(board) 
            or j < 0 
            or j == len(board[0]) 
            or board[i][j] != word[c]
            ):
            return False

        board[i][j] = "~"
        
        if (
            self.existUtil(board, word, i, j + 1, c + 1) 
            or self.existUtil(board, word, i, j - 1, c + 1)
            or self.existUtil(board, word, i + 1, j, c + 1)
            or self.existUtil(board, word, i - 1, j, c + 1)
            ):
            return True

        board[i][j] = word[c]
        
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existUtil(board, word, i, j, 0):
                    return True

        return False
# @lc code=end

