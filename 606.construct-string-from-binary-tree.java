/*
 * @lc app=leetcode id=606 lang=java
 *
 * [606] Construct String from Binary Tree
 *
 * https://leetcode.com/problems/construct-string-from-binary-tree/description/
 *
 * algorithms
 * Easy (53.15%)
 * Likes:    665
 * Dislikes: 919
 * Total Accepted:    74.9K
 * Total Submissions: 141K
 * Testcase Example:  '[1,2,3,4]'
 *
 * You need to construct a string consists of parenthesis and integers from a
 * binary tree with the preorder traversing way.
 * 
 * The null node needs to be represented by empty parenthesis pair "()". And
 * you need to omit all the empty parenthesis pairs that don't affect the
 * one-to-one mapping relationship between the string and the original binary
 * tree.
 * 
 * Example 1:
 * 
 * Input: Binary tree: [1,2,3,4]
 * ⁠      1
 * ⁠    /   \
 * ⁠   2     3
 * ⁠  /    
 * ⁠ 4     
 * 
 * Output: "1(2(4))(3)"
 * Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to
 * omit all the unnecessary empty parenthesis pairs. And it will be
 * "1(2(4))(3)".
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: Binary tree: [1,2,3,null,4]
 * ⁠      1
 * ⁠    /   \
 * ⁠   2     3
 * ⁠    \  
 * ⁠     4 
 * 
 * Output: "1(2()(4))(3)"
 * Explanation: Almost the same as the first example, except we can't omit the
 * first parenthesis pair to break the one-to-one mapping relationship between
 * the input and the output.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public String tree2strUtil(TreeNode t) {
        String combinedstr = "";

        if (t == null) {
            return combinedstr;
        }

        String leftstr = tree2strUtil(t.left);
        String rightstr = tree2strUtil(t.right);

        if (leftstr == "" && rightstr != "") {
            combinedstr = "(" + String.valueOf(t.val) + "()" + rightstr + ")";
        } else {
            combinedstr = "(" + String.valueOf(t.val) + leftstr + rightstr + ")";
        }

        return combinedstr;
    }

    public String tree2str(TreeNode t) {
        String result = "";

        if (t != null) {
            result = tree2strUtil(t);
            result = result.substring(1, result.length() - 1);
        }

        return result;
    }
}
// @lc code=end
