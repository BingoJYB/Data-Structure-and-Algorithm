import java.util.ArrayList;

/*
 * @lc app=leetcode id=98 lang=java
 *
 * [98] Validate Binary Search Tree
 */

 // @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isAscendingOrder(ArrayList<Integer> nodeVals) {
        boolean ascending = true;

        for (int i = 1; i < nodeVals.size() && ascending; i++) {
            ascending = ascending && nodeVals.get(i) > nodeVals.get(i - 1);
        }

        return ascending;
    }

    public void isValidBSTUtil(TreeNode node, ArrayList<Integer> nodeVals) {
        if (node != null) {
            isValidBSTUtil(node.left, nodeVals);
            nodeVals.add(node.val);
            isValidBSTUtil(node.right, nodeVals);
        }
    }

    public boolean isValidBST(TreeNode root) {
        ArrayList<Integer> nodeVals = new ArrayList<>();
        isValidBSTUtil(root, nodeVals);
        return isAscendingOrder(nodeVals);
    }
}
// @lc code=end
