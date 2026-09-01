class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, path, remaining):
            if remaining == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]: # dedup,易错点！：同层是i > start
                    continue
                # pruning
                if remaining - candidates[i] < 0:
                    break
                # choose
                path.append(candidates[i])
                # explore
                dfs(i + 1, path, remaining - candidates[i]) # dedup. choose at most 1 time
                # undo
                path.pop()

            return
        dfs(0, [], target)
        return res