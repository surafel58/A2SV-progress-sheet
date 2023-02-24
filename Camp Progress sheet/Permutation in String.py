class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_dict = defaultdict(int)
        s1_dict = Counter(s1)
        k = len(s1)
        n = len(s2)
        left = 0

        for right in range(n):
            s2_dict[s2[right]] += 1

            while (right - left + 1) > k:
                if s2_dict[s2[left]] == 1:
                    s2_dict.pop(s2[left])
                else:
                    s2_dict[s2[left]] -= 1

                left += 1

            if s2_dict == s1_dict:
                return True 

        return False
