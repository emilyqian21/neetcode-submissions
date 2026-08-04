class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time: O(n)
        # space: O(1)
        # greedy: start from the end, try to move the goal backwards as far as possible
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):  # taverse backwards 
            if i + nums[i] >= goal: # if at position i it can jump to the goal
                goal = i # we move the goal to i. we only need to jump to i then we can garantee we can reach the final goal
        return goal == 0