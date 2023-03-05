class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #"( () ( () ) )"
        #( 1 2 )
        result = 0
        temp = 0
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            
            elif stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                
            else:
                temp = 0
                while stack[-1] != "(":
                    temp += stack.pop()
                
                stack.pop()
                stack.append(2 * temp)
    
        while stack:
            result += stack.pop()
        
        return result    
