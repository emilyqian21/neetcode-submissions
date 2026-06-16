class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c == '+':
               stack.append(stack.pop() + stack.pop())
            elif c =='-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            
            elif c =='*':
                stack.append(stack.pop()*stack.pop())
        
            elif c =='/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a)) #int --> round towards 0
            
            else: # int
                stack.append(int(c))
        
        return stack[0]

        #time: O(n)
        #space: O(n)