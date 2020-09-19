/*
 * @lc app=leetcode id=463 lang=java
 *
 * [463] Island Perimeter
 *
 * https://leetcode.com/problems/island-perimeter/description/
 *
 * algorithms
 * Easy (62.88%)
 * Likes:    2233
 * Dislikes: 125
 * Total Accepted:    239K
 * Total Submissions: 362.6K
 * Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
 *
 * You are given row x col grid representing a map where grid[i][j] = 1
 * represents land and grid[i][j] = 0 represents water.
 * 
 * Grid cells are connected horizontally/vertically (not diagonally). The grid
 * is completely surrounded by water, and there is exactly one island (i.e.,
 * one or more connected land cells).
 * 
 * The island doesn't have "lakes", meaning the water inside isn't connected to
 * the water around the island. One cell is a square with side length 1. The
 * grid is rectangular, width and height don't exceed 100. Determine the
 * perimeter of the island.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
 * Output: 16
 * Explanation: The perimeter is the 16 yellow stripes in the image above.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[1]]
 * Output: 4
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: grid = [[1,0]]
 * Output: 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * row == grid.length
 * col == grid[i].length
 * 1 <= row, col <= 100
 * grid[i][j] is 0 or 1.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        int row = grid.length;
        int col = grid[0].length;
        boolean[][] visited = new boolean[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    perimeter = traverseIsland(grid, i, j, visited);
                }

                if (perimeter != 0) {
                    break;
                }
            }

            if (perimeter != 0) {
                break;
            }
        }

        return perimeter;
    }

    public int traverseIsland(int[][] grid, int i, int j, boolean[][] visited) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == 0 || visited[i][j]) {
            return 0;
        }

        visited[i][j] = true;
        int accumulation = 0;

        // up
        if (i == 0 || grid[i - 1][j] == 0) {
            accumulation++;
        }

        // down
        if (i == grid.length - 1 || grid[i + 1][j] == 0) {
            accumulation++;
        }

        // left
        if (j == 0 || grid[i][j - 1] == 0) {
            accumulation++;
        }

        // right
        if (j == grid[i].length - 1 || grid[i][j + 1] == 0) {
            accumulation++;
        }

        accumulation += traverseIsland(grid, i - 1, j, visited);
        accumulation += traverseIsland(grid, i + 1, j, visited);
        accumulation += traverseIsland(grid, i, j - 1, visited);
        accumulation += traverseIsland(grid, i, j + 1, visited);

        return accumulation;
    }
}
// @lc code=end

