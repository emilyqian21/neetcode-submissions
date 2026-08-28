class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack - find the next largest value 
        stack = [] # store value to be matched (number, index)
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            cur = temperatures[i]
            while stack and stack[-1][0] < cur: 
                idx = stack[-1][1]
                res[idx] = i - idx 
                stack.pop()
            stack.append([cur, i])
        return res
                
