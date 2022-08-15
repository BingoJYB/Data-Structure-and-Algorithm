/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (37.10%)
 * Likes:    14425
 * Dislikes: 3182
 * Total Accepted:    2.3M
 * Total Submissions: 6.1M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order, and each of their nodes
 * contains a single digit. Add the two numbers and return the sum as a linked
 * list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in each linked list is in the range [1, 100].
 * 0 <= Node.val <= 9
 * It is guaranteed that the list represents a number that does not have
 * leading zeros.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int overflow = 0;
        ListNode head = new ListNode(-1);
        ListNode h = head;

        while (l1 != null || l2 != null) {
            int currVal = 0;
            int l1Val = 0;
            int l2Val = 0;

            if (l1 != null) {
                l1Val = l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                l2Val = l2.val;
                l2 = l2.next;
            }

            currVal = l1Val + l2Val + overflow;
            overflow = currVal / 10;
            currVal = currVal % 10;
            h.next = new ListNode(currVal);
            h = h.next;
        }

        if (overflow == 1) {
            h.next = new ListNode(overflow);
        }

        return head.next;
    }
}
// @lc code=end

