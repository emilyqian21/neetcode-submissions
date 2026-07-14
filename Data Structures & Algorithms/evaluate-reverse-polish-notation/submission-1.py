class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # time: O(n)
        # space: O(n)
        stack = []
        for c in tokens:
            if c not in {"+", "-", "*", "/"}:
                stack.append(int(c))
            else:
                n1 = stack.pop()
                n2 = stack.pop()

                if c == "+":
                    res = n1 + n2
                    stack.append(res)

                if c == "-":
                    res = n2 - n1
                    stack.append(res)

                if c == "*":
                    res = n1 * n2
                    stack.append(res)

                if c == "/":
                    res = int(n2/n1) 
                    stack.append(res)

        return stack[-1]