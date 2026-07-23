class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # time: O(Cn · n), where Cn is the nth Catalan number.
        # space: O(n) excluding the output.
        res = []
        path = []
        choice = ["(",")"]

        def dfs(open_count, close_count):
            # if valid record answer
            if open_count == n and close_count == n:
                res.append("".join(path.copy()))
                return
            
            for i in range(len(choice)):
                # make the choice 
                #pruning
                if open_count > n or close_count > open_count:
                    # invalid
                    break # 问题 return也可以 什么时候用break,什么时候用return
                else:
                    path.append(choice[i])
                    if choice[i] == "(":
                        dfs(open_count + 1, close_count)
                    elif choice[i] == ")":
                        dfs(open_count, close_count + 1)

                # undo
                path.pop()

        dfs(0,0)
        return res
