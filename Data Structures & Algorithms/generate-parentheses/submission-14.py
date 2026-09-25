class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, openn, closen):
            # definition: traverse all valid combination of parentheses for n pairs. store historical path in path. not include current node.

            if openn == n and closen == n:
                res.append(''.join(path))
                return
            
            # choice 1: choose open parenthesis
            if openn < n:
                # choose
                path.append("(")
                # keep explore
                dfs(path, openn + 1, closen)
                # undo
                path.pop()

            # choice 2 close parenthesis
            if closen < openn:
                # choose
                path.append(")")
                # keep explore
                dfs(path, openn, closen + 1)
                #undo
                path.pop()
            
            return 
        
        dfs( [], 0, 0)
        return res

                
                