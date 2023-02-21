# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        n = 0
        nodes = []
        while curr:
            nodes.append(curr.val)
            n += 1
            curr = curr.next

        for i in range(1, n):
            temp = nodes[i]
            for j in range(i, 0, -1):
                if temp < nodes[j - 1]:
                    nodes[j], nodes[j-1] = nodes[j-1], temp

                else:
                    break   

        curr = head
        for i in range(n):
            curr.val = nodes[i]
            curr = curr.next
        
        return head
