/*
 * @lc app=leetcode id=152 lang=java
 *
 * [152] Maximum Product Subarray
 *
 * https://leetcode.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (34.83%)
 * Likes:    13484
 * Dislikes: 402
 * Total Accepted:    851.3K
 * Total Submissions: 2.4M
 * Testcase Example:  '[2,3,-2,4]'
 *
 * Given an integer array nums, find a contiguous non-empty subarray within the
 * array that has the largest product, and return the product.
 * 
 * The test cases are generated so that the answer will fit in a 32-bit
 * integer.
 * 
 * A subarray is a contiguous subsequence of the array.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [2,3,-2,4]
 * Output: 6
 * Explanation: [2,3] has the largest product 6.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [-2,0,-1]
 * Output: 0
 * Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 2 * 10^4
 * -10 <= nums[i] <= 10
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0], max = nums[0], min = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int x = Math.max(nums[i],  Math.max(max * nums[i], min * nums[i]));
            int y = Math.min(nums[i], Math.min(max * nums[i], min * nums[i]));
            max = x; 
            min = y;
            res = Math.max(res, max);
        }

        return res;
    }
}
// @lc code=end

