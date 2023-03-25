class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        solution = []
        n = len(s)

        def backtrack(index, acc):
            if len(acc) == 4:
                if ''.join(acc) == s:
                    
                    for i in range(len(acc)):
                        if not (0 <= int(acc[i]) <= 255):
                            return
                    else:
                        solution.append('.'.join(acc))
                return

            for i in range(index, n):
                val = s[index : i + 1]
                
                #avoid leading zero
                if len(val) > 1 and val[0] == '0':
                    continue

                acc.append(val)
                
                backtrack(i + 1, acc)

                acc.pop()
                
        
        backtrack(0, [])

        return solution
