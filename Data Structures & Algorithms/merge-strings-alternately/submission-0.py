class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # solution: two pointers
        # Python 的 string 是 immutable，所以反复 += 可能导致不断创建新字符串，最坏可以到 O((n+m)^2)。
        # 所以更好的做法是用list

        res = []
        l1 = 0
        l2 = 0

        while l1 < len(word1) and l2 < len(word2): # both inbound
            res.append(word1[l1])
            res.append(word2[l2])
            l1 += 1
            l2 += 1
        
        if l1 < len(word1):
            res.append(word1[l1:])

        if l2 < len(word2):
            res.append(word2[l2:])

        return "".join(res)