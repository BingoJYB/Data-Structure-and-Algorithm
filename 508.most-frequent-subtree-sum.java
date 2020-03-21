import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode id=508 lang=java
 *
 * [508] Most Frequent Subtree Sum
 *
 * https://leetcode.com/problems/most-frequent-subtree-sum/description/
 *
 * algorithms
 * Medium (56.62%)
 * Likes:    523
 * Dislikes: 103
 * Total Accepted:    63.1K
 * Total Submissions: 111.3K
 * Testcase Example:  '[5,2,-3]'
 *
 * 
 * Given the root of a tree, you are asked to find the most frequent subtree
 * sum. The subtree sum of a node is defined as the sum of all the node values
 * formed by the subtree rooted at that node (including the node itself). So
 * what is the most frequent subtree sum value? If there is a tie, return all
 * the values with the highest frequency in any order.
 * 
 * 
 * Examples 1
 * Input:
 * 
 * ⁠ 5
 * ⁠/  \
 * 2   -3
 * 
 * return [2, -3, 4], since all the values happen only once, return all of them
 * in any order.
 * 
 * 
 * Examples 2
 * Input:
 * 
 * ⁠ 5
 * ⁠/  \
 * 2   -5
 * 
 * return [2], since 2 happens twice, however -5 only occur once.
 * 
 * 
 * Note:
 * You may assume the sum of values in any subtree is in the range of 32-bit
 * signed integer.
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public int findFrequentTreeSumUtil(TreeNode root, HashMap<Integer, Integer> sumFreqMap) {
        if (root == null) {
            return 0;
        }

        int leftSum = findFrequentTreeSumUtil(root.left, sumFreqMap);
        int rightSum = findFrequentTreeSumUtil(root.right, sumFreqMap);
        int sum = root.val + leftSum + rightSum;

        if (sumFreqMap.containsKey(sum)) {
            sumFreqMap.put(sum, sumFreqMap.get(sum) + 1);
        } else {
            sumFreqMap.put(sum, 1);
        }

        return sum;
    }

    public int[] findFrequentTreeSum(TreeNode root) {
        int maxFreq = Integer.MIN_VALUE;
        List<Integer> sumWithMaxFreq = new ArrayList<>();
        HashMap<Integer, Integer> sumFreqMap = new HashMap<>();

        findFrequentTreeSumUtil(root, sumFreqMap);

        for (Map.Entry<Integer, Integer> entry : sumFreqMap.entrySet()) {
            if (entry.getValue() > maxFreq) {
                maxFreq = entry.getValue();
                sumWithMaxFreq = new ArrayList<Integer>();
                sumWithMaxFreq.add(entry.getKey());
            } else if (entry.getValue() == maxFreq) {
                sumWithMaxFreq.add(entry.getKey());
            }
        }

        int[] result = new int[sumWithMaxFreq.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = sumWithMaxFreq.get(i).intValue();
        }

        return result;
    }
}
// @lc code=end
