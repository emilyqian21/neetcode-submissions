class Solution:
    def jump(self, nums: List[int]) -> int:
        # 探索每一“跳”的所有可能性，找到最远的边界
        current_jump_farest_point= 0 
        scout_current_jump_farest_point = 0 
        jump = 0 

        for i in range(len(nums) - 1):
            # if i make the jump here, my current jump farest point is to 
            scout_current_jump_farest_point = max(nums[i]+i, scout_current_jump_farest_point) # scout一直在变化

            if i == current_jump_farest_point: # if i already reach the boundry of the farest point of this jump
                current_jump_farest_point = scout_current_jump_farest_point # i've already searched all the starting position for this jump, the scout process ends; i can determine the current_jump_farest_point
                jump += 1 

        return jump