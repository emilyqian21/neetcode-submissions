class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #edge case:
        if not digits:
            return []
        res = []
        map_dict = {"2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"], 
        "5":["j","k","l"], 
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}

        def dfs(i,path):
            #record answer if necessary: when len(path) = 2
            if len(path) == len(digits):
                res.append("".join(path.copy()))
                return 
            
            #make the choice
            for c in map_dict[digits[i]]: # digits = "34", i = 0,1, digits[i] = "3","4"
                path.append(c)
                dfs(i+1,path)
                path.pop()
            return 

        dfs(0,[])
        return res