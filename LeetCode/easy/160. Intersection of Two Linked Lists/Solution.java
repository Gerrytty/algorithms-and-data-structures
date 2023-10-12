/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        ListNode headL1 = headA;
        ListNode headL2 = headB;
        int l1 = 0;
        int l2 = 0;

        while (headL1 != null) {
            l1++;
            headL1 = headL1.next;
        }

        while (headL2 != null) {
            l2++;
            headL2 = headL2.next;
        }

        int diff = Math.abs(l1 - l2);

        ListNode a = headA;
        ListNode b = headB;

        int c = 0;

        if (l1 < l2) {
            while (b != null && c++ < diff) {
                b = b.next;
            }
        }
        else {
            while (a != null && c++ < diff) {
                a = a.next;
            }
        }

        while (a != null && b != null) {
            if (a == b) {
                return a;
            }

            a = a.next;
            b = b.next;
        }

        return null;

    }
}