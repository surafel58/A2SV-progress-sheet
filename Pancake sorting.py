class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        #a[2:4] = a[2:4][::-1]
        # n = len(arr)

        j = len(arr) - 1
        result = []
        while j >= 0:
            max = 0
            for i in range(j + 1):
                if arr[max] < arr[i]:
                    max = i

            arr[:max+1] = arr[:max+1][::-1]
            result.append(max+1)

            arr[:j+1] = arr[:j+1][::-1]
            result.append(j+1)

            j -= 1

        return result
            
