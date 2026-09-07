class Solution:
    def checkValidString(self, s: str) -> bool:
        # time: O(n)
        # space: O(1)

        # main logic: 
        # 一路维护：到当前位置为止，可能还剩多少个 unmatched "(" ，维护最大的可能性和最小的可能性
        # 当最大的可能性都小于0，说明实在是太多")”， 所以肯定不valid
        

        leftmin = 0 
        leftmax = 0

        for c in s:
            if c == "(":
                leftmin += 1
                leftmax += 1
            elif c == ")":
                leftmin -= 1
                leftmax -= 1
            elif c == "*":
                leftmin -= 1 # 把 "*" 理解为 ")"
                leftmax += 1 # 把 "*" 理解为 "("
            if leftmax < 0: # 我已经尽可能让 * 当成 ( 了，最多还能有多少个左括号, 如果连 leftmax 都 < 0，说明右括号实在太多。
                return False
            if leftmin < 0:
                leftmin = 0 # 因为 unmatched ( 的数量不可能真的是负数。
        return leftmin == 0 # 检查是否至少存在一种方案能全部配平

        # 例子： (*)
        # [leftmin, leftmax] 就会变成 [1,1]--> [0, 2] --> [-1, 1]的时候需要把leftmin改成0，--> [0, 1]