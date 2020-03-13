import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=78 lang=java
 *
 * [78] Subsets
 *
 * https://leetcode.com/problems/subsets/description/
 *
 * algorithms
 * Medium (58.10%)
 * Likes:    2971
 * Dislikes: 72
 * Total Accepted:    492.8K
 * Total Submissions: 847.1K
 * Testcase Example:  '[1,2,3]'
 *
 * Given a set of distinct integers, nums, return all possible subsets (the
 * power set).
 * 
 * Note: The solution set must not contain duplicate subsets.
 * 
 * Example:
 * 
 * 
 * Input: nums = [1,2,3]
 * Output:
 * [
 * ⁠ [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 * 
 */

// @lc code=start
class Solution {
    public void subsetsUtil(int[] nums, List<Integer> subset, int pos, List<List<Integer>> result) {
        if (pos == nums.length) {
            result.add(subset);
        } else {
            int digit = nums[pos];
            List<Integer> copiedSubset1 = new ArrayList<>(subset);
            List<Integer> copiedSubset2 = new ArrayList<>(subset);
            copiedSubset2.add(digit);
            subsetsUtil(nums, copiedSubset1, pos + 1, result);
            subsetsUtil(nums, copiedSubset2, pos + 1, result);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> subset = new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();
        subsetsUtil(nums, subset, 0, result);
        return result;
    }
}
// @lc code=end
