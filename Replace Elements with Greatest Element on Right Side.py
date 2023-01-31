class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        result = [max] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            result[i] = max
            if arr[i] > max:
                max = arr[i]

        return result
