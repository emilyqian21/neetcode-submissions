class Solution:
    def isValid(self, s: str) -> bool:
        # time: O(n)
        # space: O(n)
        stack = []
        open_to_close = {"(":")", "{":"}","[":"]"}
        
        for c in s:
            if c in open_to_close: # is an open
                stack.append(c)
            else: # is a close
                if stack:
                    pair_open = stack.pop() # the latest open
                    if c != open_to_close[pair_open]: # not the same close
                        return False
                else:
                    return False
        return len(stack) == 0
            
