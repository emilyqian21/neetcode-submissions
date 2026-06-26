class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        def ispalindrome(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start,path):#aab，我先在 a|ab，然后看 a|b 里的情况，或者 aa|b，然后看 b 的情况
            # record answer when necessary: when start == len(s)
            if start == len(s):
                res.append(path.copy())
                return
            
            # explore all possibilities
            # make decision： where to partition
            for i in range(start,len(s)):  # i 就是在哪里切，start就是这个 这次切的主体是 s[start:结尾]，比如 [aab], start = 1的话就是 [ab],i = 0,1，就是在a后面切一刀，或者ab后切一刀
                if ispalindrome(s[start:i+1]): #parts after partition
                    path.append(s[start:i+1]) 
                    #further extend the path by exploring other following options
                    dfs(i+1,path) # 往后移一格，继续探索
                    # 如果 s = [aab], start = 0 , i = 0 isp(s[0:1]) = isp([a]) dfs(start = 1, path)  --> i = 1, isp(s[1:2]) = isp([a]) dfs(start = 2,path) ------>
                                                                                                                                                                # i = 2, isp(s[2:3]) = isp([b])
                                                                                                     #  i = 2, isp(s[1:3]) = isp([ab]) dfs(start = 3) --> res.append
                                                # i = 1 isp(s[0:2]) = isp([aa]) dfs(start = 2, path)
                                                # i = 2 isp(s[0,3]) = isp([aab]) dfs(start = 3, path)

                    # undo the choice
                    path.pop()
                    #或者可以理解为： # start 表示当前这一段必须从哪里开始
                                    # i 表示当前这一段在哪里结束
                                    # 当前选择的 substring 是 s[start:i+1]
            return #return必须在for loop之外
        dfs(0,[])
        return res

        # time: O(n * 2^n), 长度为 n 的 string，有 n-1 个位置可以选择切或者不切;每次形成一个 substring / 检查 palindrome，最坏需要 O(n)
        # psace: O(n) ouptut O(n * 2^n)