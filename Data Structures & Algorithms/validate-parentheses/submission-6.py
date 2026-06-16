class Solution:
    def isValid(self, s: str) -> bool:
        stack = []#store opening
        map_dict = {"}":"{","]":"[",")":"("}
        if not s:
            return True
        for c in s:
            if c in map_dict.values(): #if c is opening
                stack.append(c)
            
            if c in map_dict: # if c is closing
                if not stack: #example s = "]"
                    return False
                if stack[-1] != map_dict[c]: # if latest opening doesn't match the current closing --> false
                    return False
                stack.pop()

        return len(stack) == 0
        
        # Time: O(n)
        # Space: O(n)