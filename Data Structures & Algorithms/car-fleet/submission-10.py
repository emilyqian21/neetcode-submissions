class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # merge from back
        fleet = 0 
        ps = [] # (position, speed)
        for p,s in zip(position, speed):
            ps.append((p, s))
        
        ps.sort(key = lambda x:x[0])

    
        prevtime = None
        for c in ps[::-1]:
            c_pos = c[0]
            c_speed = c[1]
            c_time = (target - c_pos) / c_speed
            
            if not prevtime:
                prevtime = c_time
                fleet += 1

            else:
                
                if c_time <= prevtime:
                    continue  
                else:
                    prevtime = c_time
                    fleet += 1
        return fleet
