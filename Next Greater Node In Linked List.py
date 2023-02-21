# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        n = 0
        num = []
        while curr:
            num.append(curr.val)
            curr = curr.next
            n += 1


        monoStack = []
        result = [0] * n
        
        for i in range(n):
            while monoStack and num[monoStack[-1]] < num[i]:
                result[monoStack.pop()] = num[i]

            monoStack.append(i)

        return result 
