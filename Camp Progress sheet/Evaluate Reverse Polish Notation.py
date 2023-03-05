class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        result = 0

        for token in tokens:

            if len(token) > 1 or token.isdigit():
                stack.append(token)
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                if token == "+":
                    result = operand1 + operand2
    
                elif token == "*":
                    result = operand1 * operand2

                elif token == "-":
                    result = operand1 - operand2

                else:
                    result = int(operand1 / operand2)

                stack.append(result)
        
        return int(stack[-1])
