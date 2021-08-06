class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head.next==null) return true;
        ListNode slow = head;
        ListNode fast = head.next;
        while(fast!=null){
            slow = slow.next;
            fast = fast.next==null? null : fast.next.next;
        }

        ListNode secondHalf = reverseList(slow);
        ListNode firstHalf = head;

        while(secondHalf != null && firstHalf != null){
            if(firstHalf.val != secondHalf.val) return false;
            firstHalf = firstHalf.next; secondHalf = secondHalf.next;
        }

        return true;
    }

    public ListNode reverseList(ListNode node){
        ListNode prev = null;
        ListNode curr = node;
        while(curr!=null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
}


/*
class Solution {
    public boolean isPalindrome(ListNode head) {
        ArrayList<Integer> array = new ArrayList<>();
        ListNode node = head;
        while(node!=null) {
            array.add(node.val);
            node = node.next;
        }
        return isPalindrome(array);
    }

    public boolean isPalindrome(ArrayList<Integer> array){
        int left = 0, right = array.size()-1;
        while(left<=right){
            if(array.get(left) != array.get(right)) return false;
            left++; right--;
        }
        return true;
    }
}
*/
