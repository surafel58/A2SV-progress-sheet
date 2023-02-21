# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        rotation = 0
        n = 0
        curr = head
        result = None

        #calculate size
        while curr:
            curr = curr.next
            n += 1
        
        #calculate rotation
        if k > n:
            k = k % n

        rotation = n - k

        #iterate until the node that has to be the first node
        curr = head
        for i in range(rotation):
            curr = curr.next

        #add elements starting from that node to the result
        resultCurr = None
        while curr:
            if result == None:
                result = ListNode(curr.val)
                resultCurr = result

            else:
                resultCurr.next = ListNode(curr.val)
                resultCurr = resultCurr.next

            curr = curr.next

        #add the rest of the elements before that node
        curr = head
        for i in range(rotation):
            if result == None:
                result = ListNode(curr.val)
                resultCurr = result

            else:
                resultCurr.next = ListNode(curr.val)
                resultCurr = resultCurr.next

            curr = curr.next            
        
        return result
            
