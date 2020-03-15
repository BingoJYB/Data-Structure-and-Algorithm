import java.util.Deque;
import java.util.Iterator;
import java.util.LinkedList;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=662 lang=java
 *
 * [662] Maximum Width of Binary Tree
 *
 * https://leetcode.com/problems/maximum-width-of-binary-tree/description/
 *
 * algorithms
 * Medium (39.60%)
 * Likes:    921
 * Dislikes: 207
 * Total Accepted:    48.8K
 * Total Submissions: 123.1K
 * Testcase Example:  '[1,3,2,5,3,null,9]'
 *
 * Given a binary tree, write a function to get the maximum width of the given
 * tree. The width of a tree is the maximum width among all levels. The binary
 * tree has the same structure as a full binary tree, but some nodes are null.
 * 
 * The width of one level is defined as the length between the end-nodes (the
 * leftmost and right most non-null nodes in the level, where the null nodes
 * between the end-nodes are also counted into the length calculation.
 * 
 * Example 1:
 * 
 * 
 * Input: 
 * 
 * ⁠          1
 * ⁠        /   \
 * ⁠       3     2
 * ⁠      / \     \  
 * ⁠     5   3     9 
 * 
 * Output: 4
 * Explanation: The maximum width existing in the third level with the length 4
 * (5,3,null,9).
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 
 * 
 * ⁠         1
 * ⁠        /  
 * ⁠       3    
 * ⁠      / \       
 * ⁠     5   3     
 * 
 * Output: 2
 * Explanation: The maximum width existing in the third level with the length 2
 * (5,3).
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 
 * 
 * ⁠         1
 * ⁠        / \
 * ⁠       3   2 
 * ⁠      /        
 * ⁠     5      
 * 
 * Output: 2
 * Explanation: The maximum width existing in the second level with the length
 * 2 (3,2).
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: 
 * 
 * ⁠         1
 * ⁠        / \
 * ⁠       3   2
 * ⁠      /     \  
 * ⁠     5       9 
 * ⁠    /         \
 * ⁠   6           7
 * Output: 8
 * Explanation:The maximum width existing in the fourth level with the length 8
 * (6,null,null,null,null,null,null,7).
 * 
 * 
 * 
 * 
 * Note: Answer will in the range of 32-bit signed integer.
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        int result = 1;
        Deque<TreeNode> queue = new LinkedList<>();

        if (root == null) {
            return 0;
        }

        root.val = 1;
        queue.addLast(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            Deque<TreeNode> tempQueue = new LinkedList<>();

            for (int i = size - 1; i >= 0; i--) {
                TreeNode node = queue.poll();

                if (node.left != null) {
                    node.left.val = node.val * 2;
                    tempQueue.addLast(node.left);
                }

                if (node.right != null) {
                    node.right.val = node.val * 2 + 1;
                    tempQueue.addLast(node.right);
                }
            }

            if (!tempQueue.isEmpty()) {
                TreeNode firstNotNullNode = tempQueue.getFirst();
                TreeNode lastNotNullNode = tempQueue.getLast();

                if (firstNotNullNode != null && lastNotNullNode != null) {
                    int width = lastNotNullNode.val - firstNotNullNode.val + 1;

                    if (width > result) {
                        result = width;
                    }
                }
            }

            queue.addAll(tempQueue);
        }

        return result;
    }
}
// @lc code=end
