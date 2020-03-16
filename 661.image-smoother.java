/*
 * @lc app=leetcode id=661 lang=java
 *
 * [661] Image Smoother
 *
 * https://leetcode.com/problems/image-smoother/description/
 *
 * algorithms
 * Easy (50.57%)
 * Likes:    218
 * Dislikes: 970
 * Total Accepted:    44.4K
 * Total Submissions: 87.8K
 * Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
 *
 * Given a 2D integer matrix M representing the gray scale of an image, you
 * need to design a smoother to make the gray scale of each cell becomes the
 * average gray scale (rounding down) of all the 8 surrounding cells and
 * itself.  If a cell has less than 8 surrounding cells, then use as many as
 * you can.
 * 
 * Example 1:
 * 
 * Input:
 * [[1,1,1],
 * ⁠[1,0,1],
 * ⁠[1,1,1]]
 * Output:
 * [[0, 0, 0],
 * ⁠[0, 0, 0],
 * ⁠[0, 0, 0]]
 * Explanation:
 * For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
 * For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
 * For the point (1,1): floor(8/9) = floor(0.88888889) = 0
 * 
 * 
 * 
 * Note:
 * 
 * The value in the given matrix is in the range of [0, 255].
 * The length and width of the given matrix are in the range of [1, 150].
 * 
 * 
 */

// @lc code=start
class Solution {
    public int imageSmootherUtil(int[][] matrix, int row, int col) {
        int sum = 0, counter = 0;
        int[][] pos = { { 0, 0 }, { 1, 0 }, { 1, 1 }, { -1, 0 }, { -1, 1 }, { 1, -1 }, { -1, -1 }, { 0, 1 },
                { 0, -1 } };

        for (int i = 0; i < pos.length; i++) {
            int newX = row + pos[i][0];
            int newY = col + pos[i][1];

            if (newX >= 0 && newX < matrix.length && newY >= 0 && newY < matrix[0].length) {
                sum += matrix[newX][newY];
                counter++;
            }
        }

        return (int) (sum / counter);
    }

    public int[][] imageSmoother(int[][] M) {
        int[][] result = new int[M.length][M[0].length];

        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[i].length; j++) {
                result[i][j] = imageSmootherUtil(M, i, j);
            }
        }

        return result;
    }
}
// @lc code=end
