# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = ListNode(0,head)
        fast = ListNode(0,head)

        while slow and fast:
            slow = slow.next
            fast = fast.next if not fast.next else fast.next.next

        return slow