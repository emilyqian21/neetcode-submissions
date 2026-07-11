class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # two pass
        # 先扫一遍，找每个字母最后的位置
        # 然后再扫一遍，进行记录。当i已经到达end的时候，说明这串字符是符合要求的，可以记录

        lastindex = {}
        for i, v in enumerate(s):
            lastindex[v] = i
        
        res = []
        end = 0
        size = 0
        for i,v in enumerate(s):
            end = max(lastindex[v],end)
            size += 1
            if i == end: # 找到这串字符最后的位置了
                res.append(size)
                size = 0 # reset size to 0
        return res

