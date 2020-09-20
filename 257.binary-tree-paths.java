import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Stack;

/*
 * @lc app=leetcode id=257 lang=java
 *
 * [257] Binary Tree Paths
 *
 * https://leetcode.com/problems/binary-tree-paths/description/
 *
 * algorithms
 * Easy (49.19%)
 * Likes:    1948
 * Dislikes: 112
 * Total Accepted:    337.2K
 * Total Submissions: 649K
 * Testcase Example:  '[1,2,3,null,5]'
 *
 * Given a binary tree, return all root-to-leaf paths.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * 
 * Input:
 * 
 * ⁠  1
 * ⁠/   \
 * 2     3
 * ⁠\
 * ⁠ 5
 * 
 * Output: ["1->2->5", "1->3"]
 * 
 * Explanation: All root-to-leaf paths are: 1->2->5, 1->3
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<>();
        Stack<Integer> nodes = new Stack<>();
        traverseBinaryTree(root, nodes, paths);
        return paths;
    }

    @SuppressWarnings("unchecked")
    void traverseBinaryTree(TreeNode node, Stack<Integer> nodes, List<String> paths) {
        if (node != null && node.left == null && node.right == null) {
            String path = "";
            Iterator<Integer> iter = nodes.iterator();

            while (iter.hasNext()) {
                int nodeVal = iter.next();
                String nodeStr = String.valueOf(nodeVal);
                path += nodeStr + "->";
            }

            path += String.valueOf(node.val);
            paths.add(path);
        } else if (node != null) {
            nodes.push(node.val);
            traverseBinaryTree(node.left, (Stack<Integer>)nodes.clone(), paths);
            traverseBinaryTree(node.right, (Stack<Integer>)nodes.clone(), paths);
        }
    }
}
// @lc code=end

