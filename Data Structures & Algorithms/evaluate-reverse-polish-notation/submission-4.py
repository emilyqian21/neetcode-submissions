class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # 用来存要计算的数字

        for c in tokens:
            if c not in ["+", "-", "*", "/"]: # number
                stack.append(c)
            else:
                if stack:
                    n1 = int(stack.pop())
                    n2 = int(stack.pop())

                    if c == "+":
                        res = n1 + n2
                        stack.append(res)
                    elif c == "-":
                        res = n2 - n1
                        stack.append(res)
                    elif c == "*":
                        res = n1 * n2
                        stack.append(res)
                    else:
                        res = n2 / n1
                        stack.append(res)
    
        return int(stack[-1])