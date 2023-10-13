class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        hash = 0
        n = len(s)
        left = 1
        
        i_powers = [1]
        for i in range(1, k):
            i_powers.append(power * i_powers[i - 1])

        for i in range(k):
            val = ord(s[i]) - 97 + 1 
            hash += (val * i_powers[i])
        
        
        k_power = pow(power, k - 1)
        for right in range(k, n): 
            
            if (hash % modulo) == hashValue:
                return s[left - 1 : right]
            
            val = ord(s[right]) - 97 + 1
            preVal = ord(s[left - 1]) - 97 + 1

            hash -= preVal
            hash //= power
            hash += (val * k_power)
            # hash %= modulo
            
            left += 1
        
        if (hash % modulo) == hashValue:
            return s[left - 1 : ]
        
