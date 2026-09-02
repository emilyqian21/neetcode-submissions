class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit2letter = { "2":["a", "b", "c"], 
                        "3":["d","e","f"],
                        "4":["g","h","i"],
                        "5":["j","k","l"],
                        "6":["m","n","o"],
                        "7":["p","q","r","s"],
                        "8":["t","u","v"],
                        "9":["w","x","y","z"]
                        }
        res = []
        if not digits:
            return []

        def dfs(path,start):
            # return all possible combination of digits[start:], record the historical path in path, not incl current node       
            if start == len(digits):
                res.append("".join(path))
                return
            
            for c in digit2letter[digits[start]]:
                # make choice
                path.append(c)
                # explore
                dfs(path, start + 1)
                # undo
                path.pop()
            return 
        
        dfs([], 0)
        return res