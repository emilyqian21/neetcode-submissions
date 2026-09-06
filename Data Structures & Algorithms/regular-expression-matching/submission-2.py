class Solution:
    def isMatch(self, s: str, p: str) -> bool:
# Time: O(mn), because there are at most m × n unique (i, j) states and each state is computed once due to memoization.

# Space: O(mn) for the memoization cache, plus O(m+n) recursion stack, so overall O(mn).
        
        # dfs definition: dfs(i, j) --> s[i:] 能不能被 p[j:] 完整匹配


        cache = {}  # (i, j): True / False

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # both finished
            if i >= len(s) and j >= len(p):
                return True

            # 如果能走到这里，说明 i < len(s) but j >= len(p)  --> pattern finished but s still has chars
            if j >= len(p):
                return False

            # does current char match?
            match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            # case 1: next char is "*" 要先判断是否有*
            if j + 1 < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (
                    dfs(i, j + 2)   # use 0 occurrence,  s = "aab", p = "a*b", i = 0, j = 0, j + 1 = "*"，但不用，就变成 s = "aab" , p = "b"
                    or
                    (match and dfs(i + 1, j))  # use 1+ occurrences s = "ab", p = "a*b", j = 0，因为可以继续匹配多次
                )

            # case 2: no "*" 如果没有*的话 就看是否match
            else:
                cache[(i, j)] = (
                    match and dfs(i + 1, j + 1) # s[i] == p[j] or p[j] == "." 并且 后面也match，s[i + 1:] 和p[j + 1:]也match
                )

            return cache[(i, j)]

        return dfs(0, 0)