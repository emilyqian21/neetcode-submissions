class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = [ [p,s] for p,s in zip(position,speed)]
        pos_spd.sort(key = lambda x: x[0]) # sort by position from small to largest
        # dict(sorted(dict_a.items(),key = lambda x:x[1]),reverse = True)
        
        fleet = 0
        last_time = None
        for p,s in pos_spd[::-1]:
            cur_time = (target - p) / s
            
            if not last_time:
                last_time = cur_time
                fleet += 1

            if cur_time > last_time:
                #can't catch up, new fleet
                fleet += 1
                last_time = cur_time

            # else: # can catch up. merge
            #     do nothing
                
        return fleet