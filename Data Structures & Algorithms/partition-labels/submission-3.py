class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # time: O(n)
        # space: O(26)
        lastindex = {}
        for i,v in enumerate(s):
            lastindex[v] = i
        
        # find the partition
        res = []
        size = 0
        end = 0
        for i,v in enumerate(s):
            size += 1
            end = max(end, lastindex[v])
            if i == end: # end of the partition
                res.append(size)
                size = 0
        return res