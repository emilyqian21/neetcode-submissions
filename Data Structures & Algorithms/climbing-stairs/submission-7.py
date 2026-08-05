class Solution:
    def climbStairs(self, n: int) -> int:
        # time: O(n)
        # space: O(1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev = 1
        cur = 2

        for n in range(3,n+1):
            temp_prev = prev # or prev, cur = cur, cur + prev
            prev = cur
            cur = temp_prev + cur

        return cur