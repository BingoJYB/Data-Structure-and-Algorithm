import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=119 lang=java
 *
 * [119] Pascal's Triangle II
 *
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 *
 * algorithms
 * Easy (47.11%)
 * Likes:    658
 * Dislikes: 189
 * Total Accepted:    255.3K
 * Total Submissions: 541.4K
 * Testcase Example:  '3'
 *
 * Given a non-negative index k where k ≤ 33, return the k^th index row of the
 * Pascal's triangle.
 * 
 * Note that the row index starts from 0.
 * 
 * 
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it.
 * 
 * Example:
 * 
 * 
 * Input: 3
 * Output: [1,3,3,1]
 * 
 * 
 * Follow up:
 * 
 * Could you optimize your algorithm to use only O(k) extra space?
 * 
 */

// @lc code=start
class Solution {
    public List<Integer> getRow(int rowIndex) {
        Integer[][] matrix = new Integer[rowIndex + 1][rowIndex + 1];

        for (int i = 0; i < rowIndex + 1; i++) {
            matrix[i][0] = 1;
            matrix[i][i] = 1;

            for (int j = 1; j < i; j++) {
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j];
            }
        }

        List<Integer> result = Arrays.asList(matrix[rowIndex]);
        return result;
    }
}
// @lc code=end
