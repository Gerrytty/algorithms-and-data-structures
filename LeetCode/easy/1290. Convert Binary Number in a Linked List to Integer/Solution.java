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
    public int getDecimalValue(ListNode head) {
        ListNode saved = head;

        int ans = 0;

        int c = 0;
        while (saved != null) {
            saved = saved.next;
            c++;
        }

        while (head != null) {
            ans += Math.pow(2, --c) * head.val;
            head = head.next;
        }

        return ans;
    }
}