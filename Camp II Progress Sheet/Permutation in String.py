class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        s1_freq = Counter(s1)
        s2_freq = defaultdict(int)

        for right in range(len(s2)):

            s2_freq[s2[right]] += 1

            while (right - left + 1) > len(s1):
                if s2_freq[s2[left]] == 1:
                    s2_freq.pop(s2[left]) 
                
                else:
                    s2_freq[s2[left]] -= 1
                
                left += 1

            if s1_freq == s2_freq:
                return True

        return False
