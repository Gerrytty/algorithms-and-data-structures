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

    private int max = 0;

    public void order(TreeNode root, int c) {

        if (root == null) {
            return;
        }

        order(root.left, c+1);
        order(root.right, c+1);

        max = Math.max(max, c+1);
    }

    public int maxDepth(TreeNode root) {
        order(root, 0);

        return max;
    }
}