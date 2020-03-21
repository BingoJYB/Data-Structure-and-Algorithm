import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode id=89 lang=java
 *
 * [89] Gray Code
 *
 * https://leetcode.com/problems/gray-code/description/
 *
 * algorithms
 * Medium (47.93%)
 * Likes:    547
 * Dislikes: 1429
 * Total Accepted:    153.6K
 * Total Submissions: 320.2K
 * Testcase Example:  '2'
 *
 * The gray code is a binary numeral system where two successive values differ
 * in only one bit.
 * 
 * Given a non-negative integer n representing the total number of bits in the
 * code, print the sequence of gray code. A gray code sequence must begin with
 * 0.
 * 
 * Example 1:
 * 
 * 
 * Input: 2
 * Output: [0,1,3,2]
 * Explanation:
 * 00 - 0
 * 01 - 1
 * 11 - 3
 * 10 - 2
 * 
 * For a given n, a gray code sequence may not be uniquely defined.
 * For example, [0,2,3,1] is also a valid gray code sequence.
 * 
 * 00 - 0
 * 10 - 2
 * 11 - 3
 * 01 - 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 0
 * Output: [0]
 * Explanation: We define the gray code sequence to begin with 0.
 * A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
 * 1.
 * Therefore, for n = 0 the gray code sequence is [0].
 * 
 * 
 */

// @lc code=start
class Solution {
    public int grayCodeUtil(List<Integer> binary) {
        int sum = 0;

        for (int i = 0; i < binary.size(); i++) {
            int pow = 1 << binary.size() - 1 - i;
            sum += binary.get(i) * pow;
        }

        return sum;
    }

    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        List<List<Integer>> codes = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (codes.size() == 0) {
                List<Integer> code = new ArrayList<>();
                code.add(0);
                codes.add(code);

                code = new ArrayList<>();
                code.add(1);
                codes.add(code);
            } else {
                int size = codes.size();

                for (int j = 0; j < size; j++) {
                    List<Integer> base = codes.remove(0);

                    if (j % 2 == 0) {
                        List<Integer> code = new ArrayList<>(base);
                        code.add(0);
                        codes.add(code);

                        code = new ArrayList<>(base);
                        code.add(1);
                        codes.add(code);
                    } else {
                        List<Integer> code = new ArrayList<>(base);
                        code.add(1);
                        codes.add(code);

                        code = new ArrayList<>(base);
                        code.add(0);
                        codes.add(code);
                    }
                }
            }
        }

        for (int i = 0; i < codes.size(); i++) {
            result.add(grayCodeUtil(codes.get(i)));
        }

        return result.size() == 0 ? Arrays.asList(new Integer[] { 0 }) : result;
    }
}
// @lc code=end
