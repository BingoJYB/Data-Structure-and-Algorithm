import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
 * @lc app=leetcode id=234 lang=java
 *
 * [234] Palindrome Linked List
 *
 * https://leetcode.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (38.04%)
 * Likes:    2516
 * Dislikes: 325
 * Total Accepted:    362.8K
 * Total Submissions: 952.3K
 * Testcase Example:  '[1,2]'
 *
 * Given a singly linked list, determine if it is a palindrome.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2
 * Output: false
 * 
 * Example 2:
 * 
 * 
 * Input: 1->2->2->1
 * Output: true
 * 
 * Follow up:
 * Could you do it in O(n) time and O(1) space?
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> arr = new ArrayList<Integer>();

        while (head != null) {
            arr.add(head.val);
            head = head.next;
        }

        List<Integer> originalArr = new ArrayList<>(arr);
        Collections.reverse(arr);
        return originalArr.equals(arr);
    }
}
// @lc code=end
