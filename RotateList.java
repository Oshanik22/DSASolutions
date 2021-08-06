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
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null) return null;
        ListNode node,first,second;
        first=node=second=head;
        int count = 0; int length = 0;

        while(node != null){node = node.next; length++;}
        k = k%length;

        while(first!=null && count !=k){
            first = first.next; count++;

        }
        while(first.next != null){
            first = first.next;
            second = second.next;
        }

        first.next = head;
        head = second.next;
        second.next = null;

        return head;

    }
}
