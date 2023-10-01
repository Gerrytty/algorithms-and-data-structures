class Solution {
    public ListNode deleteDuplicates(ListNode head) {

        if (head == null) {
            return head;
        }

        ListNode saved = head;

        while (head.next != null) {

            if (head.next.val == head.val) {
                head.next = head.next.next;
            }
            else {
                head = head.next;
            }
        }

        return saved;
    }
}