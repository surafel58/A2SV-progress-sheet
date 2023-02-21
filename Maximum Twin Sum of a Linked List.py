# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        reverseHead = None

        curr = head
        while curr:
            if reverseHead == None:
                reverseHead = ListNode(curr.val)

            else:
                newNode = ListNode(curr.val, reverseHead)
                reverseHead = newNode

            curr = curr.next


        slow = head
        fast = head
        curr = reverseHead

        while fast:
            maxSum = max(maxSum, slow.val + curr.val)
            fast = fast.next.next
            slow = slow.next
            curr = curr.next


        return maxSum
