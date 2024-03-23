# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid
        # reverse second half
        # 2 pointers - start and end

        # result.next = 
        fast,slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head1 = head
        head2 = prev

        result = ListNode()

        while head2.next:
            temp1 = head1.next
            head1.next = head2
            head1 = temp1

            temp2 = head2.next
            head2.next = head1
            head2 = temp2
            
