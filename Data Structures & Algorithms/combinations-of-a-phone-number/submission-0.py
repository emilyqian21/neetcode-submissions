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

        def dfs(input_digit,path):
            #record answer if necessary: when len(path) = 2
            if len(path) == len(digits):
                res.append("".join(path.copy()))
                return 
            
            #make the choice
            for i in range(len(input_digit)) : # digits = "34", i = 0,1, digits[i] = "3","4"
                for j in map_dict[input_digit[i]]: #j = "d","e","f"
                    path.append(j) # path = ["3"]
                    dfs(input_digit[i+1:],path) # i = 1

                    #undo the decision
                    path.pop()
            return 
        dfs(digits,[])
        return res