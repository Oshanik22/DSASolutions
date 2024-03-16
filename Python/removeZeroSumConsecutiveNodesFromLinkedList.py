# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        node = head
        currSum = 0
        sums = {0:dummy}

        while node:
            currSum += node.val
            if currSum in sums:
                prev = sums[currSum]
                temp = prev.next
                temp_sum = currSum
                while temp != node:
                    temp_sum += temp.val
                    temp = temp.next
                    del sums[temp_sum]
                prev.next = node.next
            else:
                sums[currSum] = node
            node = node.next
        return dummy.next