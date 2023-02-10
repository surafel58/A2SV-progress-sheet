class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        k = 0
        n = len(chars)
        while j < n:
            if chars[i] == chars[j]:
                j += 1
            else:
                if j - i == 1:
                    chars[k] = chars[i]
                    k += 1
                elif j - i > 9:
                    freq = str(j - i)
                    chars[k] = chars[i]
                    k += 1
                    for digit in freq:
                        chars[k] = digit
                        k += 1
                else:
                    freq = str(j - i)
                    chars[k] = chars[i]
                    chars[k+1] = freq
                    k += 2

                i = j
        

        if j - i == 1:
            chars[k] = chars[i]
            k += 1
        elif j - i > 9:
            freq = str(j - i)
            chars[k] = chars[i]
            k += 1
            for digit in freq:
                chars[k] = digit
                k += 1
        else:
            freq = str(j - i)
            chars[k] = chars[i]
            chars[k+1] = freq
            k += 2

        return k
