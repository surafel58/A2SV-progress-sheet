class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        s_dict = defaultdict(int)
        p_dict = Counter(p)
        k = len(p)
        n = len(s)
        left = 0
        result = []

        for right in range(n):
            s_dict[s[right]] += 1

            while (right - left + 1) > k:
                if s_dict[s[left]] == 1:
                    s_dict.pop(s[left])
                else:
                    s_dict[s[left]] -= 1

                left += 1

            if s_dict == p_dict:
                result.append(left)

        return result

                

        
