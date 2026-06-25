class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opencount, closecount,path):
            #record if necessary : 当 opencount == closecount == n 
            if opencount == closecount == n:
                res.append("".join(path.copy()))
                return

            #每个决定都有条件
            #choice A = 加 "("    
            #只有当 opencount < n 的时候才能加
            if opencount < n:
                path.append("(")
                dfs(opencount+1,closecount,path) 
                path.pop() #不用恢复opencount， 因为opencount是immutable的，所以每个stack都是存的当时的数字，它不是修改原来的变量，而是作为新的参数传给下一层。

            #choice B = 加 ")"
            #只有当 closecount < opencount 的时候才加
            if closecount < opencount:
                path.append(")")
                dfs(opencount,closecount+1,path)
                path.pop()
            
        dfs(0,0,[])
        return res

#模版：当每一步都只有2个选定的时候：要么选A 要么选B，那么就用这个模版，不需要用for loop
#choice A
# dfs
# undo

# choice B
# dfs
# undo
