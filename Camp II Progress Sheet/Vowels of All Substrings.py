class Solution:
    def countVowels(self, word):
        # Counter for storing the result of the number of substrings that contain vowels
        result = 0
        
        # Total substrings
        total_substring = len(word) * (len(word) + 1) // 2
        
        # Set of vowels
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        # Iterate through the string and calculate the number of substrings that contain vowels
        for i in range(len(word)):
            if word[i] in vowels:
                # Calculate the number of substrings that contain the current vowel character at each iteration
                result += (total_substring - (self.substrWithoutChar(i - 0) + self.substrWithoutChar((len(word) - 1) - i)))
        
        # Return the result
        return result
    
    # Calculate the total amount of substrings without containing the given vowel character
    def substrWithoutChar(self, n):
        return n * (n + 1) // 2
