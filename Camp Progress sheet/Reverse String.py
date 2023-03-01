class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)

    def reverse(self, s, left, right):
        if left >= right:
            return s


        s[left], s[right] = s[right], s[left]
        
        return self.reverse(s, left + 1, right - 1)
