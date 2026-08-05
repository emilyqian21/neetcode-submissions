class Solution:
    def checkValidString(self, s: str) -> bool:
        # time: O(n)
        # space: O(1)
        leftmin = 0 
        leftmax = 0

        for c in s:
            if c == "(":
                leftmin += 1
                leftmax += 1
            elif c == ")":
                leftmin -= 1
                leftmax -= 1
            elif c == "*":
                leftmin -= 1
                leftmax += 1
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0
        return leftmin == 0