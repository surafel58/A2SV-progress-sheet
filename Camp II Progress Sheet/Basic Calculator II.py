class Solution:
    def calculate(self, s):
        s = s.replace(" ", "")
        postfixS = self.infixToPostfix(s).split(" ")
        result = self.evalRPN(postfixS)
        return result

    def Prec(self, ch):
        if ch in ['+', '-']:
            return 1
        elif ch in ['*', '/']:
            return 2
        else:
            return -1

    def infixToPostfix(self, exp):
        result = []
        stack = []
        i = 0
        while i < len(exp):
            if exp[i] == '-' and (i == 0 or (i > 0 and not exp[i-1].isdigit())):
                num = '-'
                i += 1
                while i < len(exp) and exp[i].isdigit():
                    num += exp[i]
                    i += 1
                result.append(num)
            elif exp[i].isdigit():
                num = ''
                while i < len(exp) and exp[i].isdigit():
                    num += exp[i]
                    i += 1
                result.append(num)
            else:
                while stack and self.Prec(exp[i]) <= self.Prec(stack[-1]):
                    result.append(stack.pop())
                stack.append(exp[i])
                i += 1

        while stack:
            result.append(stack.pop())

        return " ".join(result)

    def evalRPN(self, tokens):
        operands = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = operands.pop()
                a = operands.pop()
                if token == '+':
                    operands.append(a + b)
                elif token == '-':
                    operands.append(a - b)
                elif token == '*':
                    operands.append(a * b)
                elif token == '/':
                    operands.append(int(float(a) / b))
            else:
                operands.append(int(token))
        result = operands.pop()
        return result
