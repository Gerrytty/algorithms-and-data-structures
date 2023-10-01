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
    public ListNode deleteDuplicates(ListNode head) {

        if (head == null) {
            return head;
        }

        ListNode saved = head;
        ListNode curr = head;

        int currVal = head.val;

        while (head != null) {

            while (curr != null && curr.val == currVal) {
                curr = curr.next;
            }

            if (curr != null) {
                currVal = curr.val;
            }


            head.next = curr;
            head = head.next;
        }

        return saved;
    }
}