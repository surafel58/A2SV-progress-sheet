class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        result = self.winner(nums, 0, len(nums)-1, True)

        if result >= 0:
            return True
        return False

    def winner(self, nums, start, end, turn):
        if start == end:
            if turn:
                return nums[start]
            return -nums[start]

        left = nums[start]
        right = nums[end]

        if not turn:
            left *= -1
            right *= -1

        left += self.winner(nums, start + 1, end, not turn)
        right += self.winner(nums, start, end - 1, not turn)

        if not turn:
            return min(left, right)

        return max(left, right) 

    
