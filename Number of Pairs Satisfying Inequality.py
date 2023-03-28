class Solution:
    def __init__(self):
        self.result = 0
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        difference = []

        for i in range(len(nums1)):
            difference.append(nums1[i] - nums2[i])
        # print(difference)
        self.findPairs(difference, diff, 0, len(nums1) - 1)
        return self.result

    def findPairs(self, difference,diff, s, e):
        
        if s == e:
            return [difference[s]]

        mid = s + (e - s) // 2
        left = self.findPairs(difference, diff, s, mid)
        right = self.findPairs(difference, diff, mid + 1, e)

        merged = []

        p1 = 0

        #using a pointer to count the valid pairs (fix right element and iterate the left array)
        for j in range(len(right)):
            target = right[j] + diff

            while p1 < len(left) and left[p1] <= target:
                p1 += 1
            
            self.result += p1

        p1 = 0
        p2 = 0

        #merge to sorted array
        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                merged.append(left[p1])
                p1 += 1

            else:
                merged.append(right[p2])
                p2 += 1

        merged.extend(left[p1:])
        merged.extend(right[p2:])
        
        return merged

