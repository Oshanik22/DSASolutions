# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx = 0
        node = list1

        breakStart = ListNode()
        breakEnd = ListNode()

        while node:
            if idx == a-1:
                breakStart = node
            elif idx == b+1:
                breakEnd = node
            node = node.next
            idx += 1
        
        endList2 = list2

        while endList2.next:
            endList2 = endList2.next

        breakStart.next = list2
        endList2.next = breakEnd

        return list1