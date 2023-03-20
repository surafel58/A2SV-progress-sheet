class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        letter_freq = defaultdict(int)
        n = len(s)
        left = 0
        maxLen = 0

        for right in range(n):
            letter_freq[s[right]] += 1

            while (right - left + 1) - max(letter_freq.values()) > k:
                letter_freq[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen
