class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for sign in tokens:
            if sign not in "+-*/":
                stack.append(int(sign))
            else:
                b = stack.pop()
                a = stack.pop()
                if sign == "+":
                    stack.append(a+b)
                elif sign == "-":
                    stack.append(a-b)
                elif sign == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[0]
        