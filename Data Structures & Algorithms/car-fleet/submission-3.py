class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # 存到达目的地的时间，如果比上一辆车到达的时间短，说明有collision，说明是fleet
        
        car_pos_speed = [ [p,s] for p, s in zip(position, speed)]
        car_pos_speed.sort( key = lambda x:x[0]) # 按position 从小到大排


        for p,s in car_pos_speed[::-1]:
            cur_time =  (target - p)/s
            if not stack or cur_time > stack[-1]: # 无collision
                stack.append(cur_time)
        return len(stack)
