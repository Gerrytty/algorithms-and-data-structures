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

    public boolean inorder(TreeNode left, TreeNode right) {

        if (left == null && right == null) {
            return true;
        }

        if (left == null || right == null) {
            return false;
        }

        boolean first = inorder(left.left, right.right);

        if ((left.val != right.val) || !first) {
            return false;
        }

        return inorder(left.right, right.left);

    }

    public boolean isSymmetric(TreeNode root) {
        return inorder(root, root);
    }
}