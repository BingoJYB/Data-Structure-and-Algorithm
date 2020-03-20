import java.util.HashMap;

/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 *
 * https://leetcode.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (55.25%)
 * Likes:    1193
 * Dislikes: 130
 * Total Accepted:    492.4K
 * Total Submissions: 889.6K
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * Given two strings s and t , write a function to determine if t is an anagram
 * of s.
 * 
 * Example 1:
 * 
 * 
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "rat", t = "car"
 * Output: false
 * 
 * 
 * Note:
 * You may assume the string contains only lowercase alphabets.
 * 
 * Follow up:
 * What if the inputs contain unicode characters? How would you adapt your
 * solution to such case?
 * 
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sh = new HashMap<>();
        HashMap<Character, Integer> th = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            int count = sh.containsKey(s.charAt(i)) ? sh.get(s.charAt(i)) : 0;
            sh.put(s.charAt(i), count + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            int count = th.containsKey(t.charAt(i)) ? th.get(t.charAt(i)) : 0;
            th.put(t.charAt(i), count + 1);
        }

        return sh.equals(th);
    }
}
// @lc code=end
