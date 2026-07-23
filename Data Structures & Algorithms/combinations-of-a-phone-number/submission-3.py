class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Time: O(n · 4ⁿ) because we generate up to 4 choices for each of the n digits, and constructing each result string costs O(n). 
        # Space:  auxiliary O(n); output O(n · 4ⁿ).
        num2digit = {
                    "2":["a","b","c"],"3":["d","e","f"],
                    "4":["g","h","i"],"5":["j","k","l"],
                    "6":["m","n","o"],"7":["p","q","r","s"],
                    "8":["t","u","v"],"9":["w","x","y","z"]
                    }
        res = []
        path = []
        #edge case
        if not digits:
            return []

        def dfs(start):
            # when to record answer
            if start == len(digits):
                word = "".join(path)
                res.append(word)
                return

            # choices 
            for c in num2digit[digits[start]]:
                path.append(c) # path = ["d","g"]

                # keep exploring the path
                dfs(start + 1)

                #undo
                path.pop()
        dfs(0)
        return res
