class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       
        fruits_freq = defaultdict(int)
        maxLen = 0
        left = 0

        n = len(fruits)

        for right in range(n):
            fruits_freq[fruits[right]] += 1

            while len(fruits_freq) > 2:
                fruits_freq[fruits[left]] -= 1

                if fruits_freq[fruits[left]] == 0:
                    fruits_freq.pop(fruits[left])

                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen
