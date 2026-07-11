class Solution:
    def checkValidString(self, s: str) -> bool:
        # 记录left_min, left_max；如果left_max < 0, 那么肯定是false; 如果left_min <0， 我们reset到0，无法做判断因为left_max > 0; 最后看left_min是否 == 0
        # time: O(n)
        # space: O(1)
        left_min = 0
        left_max = 0 

        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min -= 1
                left_max -= 1
            else: # *
                left_min -= 1 # can be ")"
                left_max += 1 # can be "("
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0