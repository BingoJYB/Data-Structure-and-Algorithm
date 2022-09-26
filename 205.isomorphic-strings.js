/*
 * @lc app=leetcode id=205 lang=javascript
 *
 * [205] Isomorphic Strings
 *
 * https://leetcode.com/problems/isomorphic-strings/description/
 *
 * algorithms
 * Easy (42.44%)
 * Likes:    4885
 * Dislikes: 897
 * Total Accepted:    648.2K
 * Total Submissions: 1.5M
 * Testcase Example:  '"egg"\n"add"'
 *
 * Given two strings s and t, determine if they are isomorphic.
 * 
 * Two strings s and t are isomorphic if the characters in s can be replaced to
 * get t.
 * 
 * All occurrences of a character must be replaced with another character while
 * preserving the order of characters. No two characters may map to the same
 * character, but a character may map to itself.
 * 
 * 
 * Example 1:
 * Input: s = "egg", t = "add"
 * Output: true
 * Example 2:
 * Input: s = "foo", t = "bar"
 * Output: false
 * Example 3:
 * Input: s = "paper", t = "title"
 * Output: true
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 5 * 10^4
 * t.length == s.length
 * s and t consist of any valid ascii character.
 * 
 * 
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    sLength = s.length;
    tLength = t.length;
    map = new Map();
    set = new Set();

    if (sLength != tLength) return false;

    for (let i = 0; i < sLength; i++) {
        if (map[s[i]]) {
            if (map[s[i]] != t[i]) return false;
        } else {
            if (set.has(t[i])) return false;
            map[s[i]] = t[i];
            set.add(t[i]);
        }
    }

    return true;
};
// @lc code=end

