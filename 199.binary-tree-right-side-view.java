import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode id=199 lang=java
 *
 * [199] Binary Tree Right Side View
 *
 * https://leetcode.com/problems/binary-tree-right-side-view/description/
 *
 * algorithms
 * Medium (51.73%)
 * Likes:    1737
 * Dislikes: 97
 * Total Accepted:    240.2K
 * Total Submissions: 463.5K
 * Testcase Example:  '[1,2,3,null,5,null,4]'
 *
 * Given a binary tree, imagine yourself standing on the right side of it,
 * return the values of the nodes you can see ordered from top to bottom.
 * 
 * Example:
 * 
 * 
 * Input: [1,2,3,null,5,null,4]
 * Output: [1, 3, 4]
 * Explanation:
 * 
 * ⁠  1            <---
 * ⁠/   \
 * 2     3         <---
 * ⁠\     \
 * ⁠ 5     4       <---
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> queue = new LinkedList<>();
        queue.addLast(root);

        if (root == null) {
            return result;
        }

        while (!queue.isEmpty()) {
            int size = queue.size();
            Deque<TreeNode> tempQueue = new LinkedList<>();

            for (int i = size - 1; i >= 0; i--) {
                TreeNode node = queue.poll();

                if (i == size - 1) {
                    result.add(node.val);
                }

                if (node.right != null) {
                    tempQueue.addLast(node.right);
                }

                if (node.left != null) {
                    tempQueue.addLast(node.left);
                }
            }

            queue.addAll(tempQueue);
        }

        return result;
    }
}
// @lc code=end
