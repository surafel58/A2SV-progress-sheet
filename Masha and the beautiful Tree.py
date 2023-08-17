result = 0

def mergeSort(nums, start, end):
    global result
        
    if result == -1:
        return []
    
    if start == end:
        return [nums[start]]

    mid = start + (end - start) // 2

    left = mergeSort(nums, start, mid)
    right = mergeSort(nums, mid + 1, end) 

    merged = []

    if left and right:
        if left[0] >= right[-1]:
            merged = right + left
            result += 1
        elif left[-1] <= right[0]:
            merged = left + right
            # result += 1
        else:
            result = -1
            return []

    return merged

test_case = int(input())

for _ in range(test_case):
    result = 0
    m = int(input())
    leaves = list(map(int, input().split()))
    mergeSort(leaves, 0, m - 1)
    print(result)

