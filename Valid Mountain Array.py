class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        isIncreasing = True
        isDecreasing = False

        if len(arr) < 3:
            return False

        for i in range(len(arr) - 1):
            if isIncreasing and arr[i] < arr[i+1]:
                continue
            else:
                isIncreasing = False
                isDecreasing = True
            
            if i != 0 and isDecreasing and arr[i] > arr[i+1]:
                continue
            else:
                return False
        
        if not isIncreasing:
            return True
