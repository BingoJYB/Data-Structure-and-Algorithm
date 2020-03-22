import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=645 lang=java
 *
 * [645] Set Mismatch
 *
 * https://leetcode.com/problems/set-mismatch/description/
 *
 * algorithms
 * Easy (41.52%)
 * Likes:    548
 * Dislikes: 282
 * Total Accepted:    64.7K
 * Total Submissions: 155.7K
 * Testcase Example:  '[1,2,2,4]'
 *
 * 
 * The set S originally contains numbers from 1 to n. But unfortunately, due to
 * the data error, one of the numbers in the set got duplicated to another
 * number in the set, which results in repetition of one number and loss of
 * another number. 
 * 
 * 
 * 
 * Given an array nums representing the data status of this set after the
 * error. Your task is to firstly find the number occurs twice and then find
 * the number that is missing. Return them in the form of an array.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [1,2,2,4]
 * Output: [2,3]
 * 
 * 
 * 
 * Note:
 * 
 * The given array size will in the range [2, 10000].
 * The given array's numbers won't have any order.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] result = new int[2];
        HashMap<Integer, Integer> numFreqMap = new HashMap<Integer, Integer>();

        for (int i = 1; i <= nums.length; i++) {
            numFreqMap.put(i, 0);
        }

        for (int num : nums) {
            numFreqMap.put(num, numFreqMap.get(num) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : numFreqMap.entrySet()) {
            if (entry.getValue() == 2) {
                result[0] = entry.getKey();
            } else if (entry.getValue() == 0) {
                result[1] = entry.getKey();
            }
        }

        return result;
    }
}
// @lc code=end
