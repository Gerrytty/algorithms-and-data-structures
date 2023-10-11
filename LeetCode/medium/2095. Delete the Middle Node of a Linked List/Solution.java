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
    public ListNode deleteMiddle(ListNode head) {


        if (head.next == null) {
            head = null;
            return head;
        }

        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = head;

        int c = 0;

        while (fast != null && fast.next != null && fast.next.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
            c += 2;
        }

        if (fast.next == null) {
            c += 1;
        }

        if (c % 2 == 0) {
            slow.next = slow.next.next;
        }
        else {
            prev.next = slow.next;
        }


        return head;

    }
}