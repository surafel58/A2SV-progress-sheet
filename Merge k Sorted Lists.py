# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        for i in range(len(lists)):
            temp = lists[i]
            nums = []
            while temp:
                nums.append(temp.val)
                temp = temp.next
            
            heapq.heapify(nums)
            
            lists[i] = nums
        

        heapq.heapify(lists)

        temp = None
        while len(lists):

            arr = heapq.heappop(lists)

            if len(arr) != 0:            
                curr = heapq.heappop(arr)
                heapq.heappush(lists, arr)
                
                if not result:
                    result = ListNode(curr)
                    temp = result
                else:
                    temp.next = ListNode(curr)
                    temp = temp.next

        return result
