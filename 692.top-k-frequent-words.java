import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Map;

import javafx.util.Pair;

/*
 * @lc app=leetcode id=692 lang=java
 *
 * [692] Top K Frequent Words
 *
 * https://leetcode.com/problems/top-k-frequent-words/description/
 *
 * algorithms
 * Medium (49.37%)
 * Likes:    1348
 * Dislikes: 116
 * Total Accepted:    125.8K
 * Total Submissions: 254.6K
 * Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
 *
 * Given a non-empty list of words, return the k most frequent elements.
 * Your answer should be sorted by frequency from highest to lowest. If two
 * words have the same frequency, then the word with the lower alphabetical
 * order comes first.
 * 
 * Example 1:
 * 
 * Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
 * Output: ["i", "love"]
 * Explanation: "i" and "love" are the two most frequent words.
 * ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
 * "is"], k = 4
 * Output: ["the", "is", "sunny", "day"]
 * Explanation: "the", "is", "sunny" and "day" are the four most frequent
 * words,
 * ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
 * 
 * 
 * 
 * Note:
 * 
 * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 * Input words contain only lowercase letters.
 * 
 * 
 * 
 * Follow up:
 * 
 * Try to solve it in O(n log k) time and O(n) extra space.
 * 
 * 
 */

// @lc code=start
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Comparator<Pair<String, Integer>> comparator = new Comparator<Pair<String, Integer>>() {
            public int compare(Pair<String, Integer> left, Pair<String, Integer> right) {
                if (left.getValue() < right.getValue()) {
                    return 1;
                } else if (left.getValue() > right.getValue()) {
                    return -1;
                } else {
                    return left.getKey().compareTo(right.getKey());
                }
            }
        };

        List<String> result = new ArrayList<String>();
        HashMap<String, Integer> words_counter = new HashMap<String, Integer>();
        Queue<Pair<String, Integer>> max_heap = new PriorityQueue<Pair<String, Integer>>(comparator);

        for (String word : words) {
            words_counter.put(word, words_counter.getOrDefault(word, 0) + 1);
        }

        for (Map.Entry<String, Integer> word_counter : words_counter.entrySet()) {
            Pair<String, Integer> pair = new Pair<String, Integer>(word_counter.getKey(), word_counter.getValue());
            max_heap.add(pair);
        }

        for (int i = 0; i < k; i++) {
            result.add(max_heap.poll().getKey());
        }

        return result;
    }
}
// @lc code=end
