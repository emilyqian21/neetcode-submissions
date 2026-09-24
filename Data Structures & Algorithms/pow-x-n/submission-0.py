class Solution:
    def myPow(self, x: float, n: int) -> float:
        # solution: recursion 
        # dfs definition: dfs(x, n) returns the result of x^n. n can only be positive value 
        
        # time: O(log |n|)
        # space: O(1)
        
        # edge case
        if x == 0:
            return 0

        def dfs(x,n):
            # base case
            if n == 0:
                return 1

            root = dfs(x, n // 2)
            if n % 2 == 1: # odd, x^5 
                res = root * root * x
                
            else: # even, x^ 4
                res = root * root
            return res
        
        # check if n is negative
        if n < 0:
            return 1 / dfs(x, abs(n))
        else:
            return dfs(x, abs(n))