class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            if s[right] not in visited:
                visited.add(s[right])
            else:
                
                while s[right] in visited:
                    visited.remove(s[left])
                    left += 1 

                visited.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength
