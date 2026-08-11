class Solution:
    def isMatch(self, s: str, p: str) -> bool:
# Time: O(mn), because there are at most m × n unique (i, j) states and each state is computed once due to memoization.

# Space: O(mn) for the memoization cache, plus O(m+n) recursion stack, so overall O(mn).

        cache = {}  # (i, j): True / False

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # both finished
            if i >= len(s) and j >= len(p):
                return True

            # pattern finished but s still has chars
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
                    dfs(i, j + 2)                 # use 0 occurrence
                    or
                    (match and dfs(i + 1, j))    # use 1+ occurrences
                )

            # case 2: no "*" 如果没有*的话 就看是否match
            else:
                cache[(i, j)] = (
                    match and dfs(i + 1, j + 1)
                )

            return cache[(i, j)]

        return dfs(0, 0)