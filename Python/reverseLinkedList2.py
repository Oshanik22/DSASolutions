# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev = dummy
        cur = head

        for _ in range(1, left):
            cur = cur.next
            leftPrev = leftPrev.next
        
        prev = None

        for _ in range(left, right+1):
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext
        
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next