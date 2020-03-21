import java.util.HashSet;
import java.util.Iterator;

/*
 * @lc app=leetcode id=414 lang=java
 *
 * [414] Third Maximum Number
 *
 * https://leetcode.com/problems/third-maximum-number/description/
 *
 * algorithms
 * Easy (30.01%)
 * Likes:    540
 * Dislikes: 995
 * Total Accepted:    124.7K
 * Total Submissions: 414.5K
 * Testcase Example:  '[3,2,1]'
 *
 * Given a non-empty array of integers, return the third maximum number in this
 * array. If it does not exist, return the maximum number. The time complexity
 * must be in O(n).
 * 
 * Example 1:
 * 
 * Input: [3, 2, 1]
 * 
 * Output: 1
 * 
 * Explanation: The third maximum is 1.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: [1, 2]
 * 
 * Output: 2
 * 
 * Explanation: The third maximum does not exist, so the maximum (2) is
 * returned instead.
 * 
 * 
 * 
 * Example 3:
 * 
 * Input: [2, 2, 3, 1]
 * 
 * Output: 1
 * 
 * Explanation: Note that the third maximum here means the third maximum
 * distinct number.
 * Both numbers with value 2 are both considered as second maximum.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int thirdMax(int[] nums) {
        HashSet<Integer> hs = new HashSet<Integer>();
        int[] smallArr = { Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE };

        for (int num : nums) {
            hs.add(num);
        }

        Iterator<Integer> it = hs.iterator();
        if (hs.size() >= 3) {
            while (it.hasNext()) {
                smallArr[3] = it.next();

                for (int i = 3; i > 0; i--) {
                    if (smallArr[i] > smallArr[i - 1]) {
                        int temp = smallArr[i - 1];
                        smallArr[i - 1] = smallArr[i];
                        smallArr[i] = temp;
                    } else {
                        break;
                    }
                }
            }

            return smallArr[2];
        } else if (hs.size() == 2) {
            int first = it.next();
            int second = it.next();
            return first > second ? first : second;
        } else {
            return it.next();
        }
    }
}
// @lc code=end
