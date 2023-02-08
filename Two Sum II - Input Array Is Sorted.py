class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        indices = []
        while left < right:
            if target > (numbers[left] + numbers[right]):
                left += 1
            elif target < (numbers[left] + numbers[right]):
                right -= 1
            else:
                indices.append(left + 1)
                indices.append(right + 1)
                break

        return indices
                
