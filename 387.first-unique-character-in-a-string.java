import java.util.HashMap;
import java.util.HashSet;

/*
 * @lc app=leetcode id=387 lang=java
 *
 * [387] First Unique Character in a String
 *
 * https://leetcode.com/problems/first-unique-character-in-a-string/description/
 *
 * algorithms
 * Easy (51.54%)
 * Likes:    1548
 * Dislikes: 101
 * Total Accepted:    405.4K
 * Total Submissions: 785.8K
 * Testcase Example:  '"leetcode"'
 *
 * 
 * Given a string, find the first non-repeating character in it and return it's
 * index. If it doesn't exist, return -1.
 * 
 * Examples:
 * 
 * s = "leetcode"
 * return 0.
 * 
 * s = "loveleetcode",
 * return 2.
 * 
 * 
 * 
 * 
 * Note: You may assume the string contain only lowercase letters.
 * 
 */

// @lc code=start
class Solution {
    public int firstUniqChar(String s) {
        int result = Integer.MAX_VALUE;
        HashSet<Character> hs = new HashSet<Character>();
        HashMap<Character, Integer> hm = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (hs.contains(c)) {
                continue;
            }

            if (!hm.containsKey(c)) {
                hm.put(c, i);
            } else {
                hm.remove(c);
                hs.add(c);
            }
        }

        for (Integer index : hm.values()) {
            result = result < index ? result : index;
        }

        return result == Integer.MAX_VALUE ? -1 : result;
    }
}
// @lc code=end
