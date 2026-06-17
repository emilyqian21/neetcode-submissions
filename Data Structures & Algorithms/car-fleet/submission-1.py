class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p,s] for p,s in  zip (position, speed)] # [[p1,s1],[p2,s2]]
        pair = sorted(pair) #按照position排序
        for p,s in pair[::-1]: # 从后往前
            time = (target - p) / s
            stack.append(time) # now time is the stack[-1]
            if len(stack) > 1 and stack[-1] <= stack[-2]: # cur_car takes less time than last car to arrive destination
                stack.pop()
        
        return len(stack)