class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # pattern: find next greater value
        # soution: monotonic stack

        # time: O(n)
        # space: O(n)

        res = [0] * len(temperatures) # initialize with 0 as default ans
        stack = [] # [[temperature, index]]
        for i,t in enumerate(temperatures): # 用while, 不用for, 因为要一直match到不能match为止 71 72 74
            while stack and stack[-1][0] < t: # the last element in stack, the [0] is the temperature 
                #temperature[i] is the next larger value for stack[-1]
                t_stack, i_stack = stack.pop()
                res[i_stack] = i - i_stack

            stack.append([t,i])
        return res