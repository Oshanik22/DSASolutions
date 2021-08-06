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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode node = head;
        int count=0;
        while(node != null && count !=k){
            node = node.next;
            count++;
        }

        //If the list has more than k elements
        if(count==k){
            ListNode rest_head = reverseKGroup(node, k);

            ListNode prev = null;
            ListNode curr = head;

            while(count-->0){
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }

            head.next = rest_head;

            return prev;
        }

        return head;
    }
}
