/*
 * @lc app=leetcode id=200 lang=java
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (44.90%)
 * Likes:    4299
 * Dislikes: 158
 * Total Accepted:    568.7K
 * Total Submissions: 1.3M
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of
 * islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically. You may assume all four edges of
 * the grid are all surrounded by water.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * Output: 3
 * 
 */

// @lc code=start
class Solution {
    public void numIslandsUtil(char[][] grid, int row, int col, boolean[][] isVisited) {
        if (row >= 0 && row < grid.length && col >= 0 && col < grid[0].length && grid[row][col] == '1'
                && !isVisited[row][col]) {
            isVisited[row][col] = true;
            numIslandsUtil(grid, row, col - 1, isVisited);
            numIslandsUtil(grid, row, col + 1, isVisited);
            numIslandsUtil(grid, row - 1, col, isVisited);
            numIslandsUtil(grid, row + 1, col, isVisited);
        }
    }

    public int numIslands(char[][] grid) {
        int numOfIslands = 0;

        if (grid.length == 0) {
            return numOfIslands;
        }

        boolean[][] isVisited = new boolean[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1' && isVisited[i][j] == false) {
                    numIslandsUtil(grid, i, j, isVisited);
                    numOfIslands += 1;
                }
            }
        }

        return numOfIslands;
    }
}
// @lc code=end
