/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head == null) return null;
        if(head.next == null) return null;
        ListNode slow = head.next;
        ListNode fast = head.next.next;

        while(fast != slow){
            if(fast==null) return null;
            fast = fast.next==null? null : fast.next.next;
            slow = slow.next;
        }
        fast = head;
        while(fast != slow){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;

    }
}
