/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/add-two-numbers/
 */
import java.math.BigInteger;
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode head = new ListNode();
        
        ListNode current = head;
        
        int sum = 0;
        int prevIncrement = 0;
        while (l1 != null || l2 != null || prevIncrement > 0) {
            sum = 0;
            if (l1 != null) {
                sum += l1.val;
            }
            if (l2 != null) {
                sum += l2.val;
            }
            sum += prevIncrement;
            prevIncrement = sum / 10;
                        
            if (sum >= 10) {
                sum -= 10;
            }
                        
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
            
            current.val = sum;
            
            if (l1 != null || l2 != null || prevIncrement > 0) {
                current.next = new ListNode();
                current = current.next;
            }
        }
                
        return head;
    }
}