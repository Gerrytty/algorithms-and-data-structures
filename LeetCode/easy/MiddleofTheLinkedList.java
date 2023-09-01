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
    public ListNode middleNode(ListNode head) {

        ListNode firstPointer = head;
        ListNode secondPointer = head;

        while (true) {
            if (secondPointer == null) {
                return firstPointer;
            }
            if (secondPointer.next == null) {
                return firstPointer;
            }
            firstPointer = firstPointer.next;
            secondPointer = secondPointer.next.next;
        }

    }
}