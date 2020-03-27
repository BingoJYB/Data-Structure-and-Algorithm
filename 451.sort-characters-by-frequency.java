import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Queue;

/*
 * @lc app=leetcode id=451 lang=java
 *
 * [451] Sort Characters By Frequency
 *
 * https://leetcode.com/problems/sort-characters-by-frequency/description/
 *
 * algorithms
 * Medium (58.95%)
 * Likes:    1100
 * Dislikes: 91
 * Total Accepted:    131.9K
 * Total Submissions: 223K
 * Testcase Example:  '"tree"'
 *
 * Given a string, sort it in decreasing order based on the frequency of
 * characters.
 * 
 * Example 1:
 * 
 * Input:
 * "tree"
 * 
 * Output:
 * "eert"
 * 
 * Explanation:
 * 'e' appears twice while 'r' and 't' both appear once.
 * So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
 * answer.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input:
 * "cccaaa"
 * 
 * Output:
 * "cccaaa"
 * 
 * Explanation:
 * Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
 * Note that "cacaca" is incorrect, as the same characters must be together.
 * 
 * 
 * 
 * Example 3:
 * 
 * Input:
 * "Aabb"
 * 
 * Output:
 * "bbAa"
 * 
 * Explanation:
 * "bbaA" is also a valid answer, but "Aabb" is incorrect.
 * Note that 'A' and 'a' are treated as two different characters.
 * 
 * 
 */

// @lc code=start
class Solution {
    public String frequencySort(String s) {
        HashMap<Character, String> hm = new HashMap<>();
        Queue<String> pq = new PriorityQueue<String>(new myComparator());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            hm.put(c, hm.getOrDefault(c, "") + Character.toString(c));
        }

        for (String val : hm.values()) {
            pq.add(val);
        }

        while (pq.size() > 0) {
            sb.append(pq.poll());
        }

        return sb.toString();
    }
}

class myComparator implements Comparator<String> {
    public int compare(String s1, String s2) {
        if (s2.length() > s1.length()) {
            return 1;
        } else {
            return -1;
        }
    }
}
// @lc code=end
