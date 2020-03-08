import java.util.*;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public static ListNode getListMiddlePoint(ListNode head, ListNode tail) {
        ListNode fastPointer = head;
        ListNode slowPointer = head;

        if (tail == null) {
            while (fastPointer != null && fastPointer.next != null) {
                fastPointer = fastPointer.next.next;
                slowPointer = slowPointer.next;
            }
        } else {
            while (fastPointer.next.val != tail.val && fastPointer.val != tail.val) {
                fastPointer = fastPointer.next.next;
                slowPointer = slowPointer.next;
            }
        }

        return slowPointer;
    }

    public static TreeNode sortedListToBSTUtil(ListNode head, ListNode tail) {
        if (head == null || head == tail) {
            return null;
        }

        ListNode middle = getListMiddlePoint(head, tail);
        TreeNode root = new TreeNode(middle.val);
        root.left = sortedListToBSTUtil(head, middle);
        root.right = sortedListToBSTUtil(middle.next, tail);

        return root;
    }

    public static TreeNode sortedListToBST(ListNode head) {
        return sortedListToBSTUtil(head, null);
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(-10);
        ListNode next1 = new ListNode(-3);
        ListNode next2 = new ListNode(0);
        ListNode next3 = new ListNode(5);
        ListNode next4 = new ListNode(9);

        head.next = next1;
        next1.next = next2;
        next2.next = next3;
        next3.next = next4;

        TreeNode root = sortedListToBST(head);

        System.out.println(root);
    }
}