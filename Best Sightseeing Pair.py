class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        n = len(values)
        i_pair = []
        j_pair = []

        for i in range(n):
            i_pair.append(values[i] + i)
            j_pair.append(values[i] - i)

        max_num = i_pair[0]

        for i in range(1,n):
            if i_pair[i] > max_num:
                max_num = i_pair[i]
            else:
                i_pair[i] = max_num

        result = float('-inf')

        for i in range(n - 1, 0, -1):
            result = max(result, j_pair[i] + i_pair[i - 1])
        
        return result
