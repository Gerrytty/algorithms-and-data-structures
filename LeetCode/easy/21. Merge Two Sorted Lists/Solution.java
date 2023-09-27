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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode left;
        ListNode right;
        ListNode temp;
        ListNode head;

        if (list1 == null && list2 == null) {
            return null;
        }

        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }

        if (list1.val < list2.val) {
            left = list1;
            right = list2;
        }
        else {
            left = list2;
            right = list1;
        }

        head = left;
        ListNode parent = left;

        while (right != null) {

            while (left != null && left.val <= right.val) {
                parent = left;
                left = left.next;
            }

            temp = left;
            parent.next = right;
            left = parent;
            right = temp;

        }

        return head;

    }
}