class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # time: O(n)
        # space: O(26)

        # main logic: 
        # 当前 partition 里出现过的所有字母，都必须在这个 partition 里“结束”
        # 所以，你要不断把 partition 的右边界扩到这些字母各自的最后出现位置。

        lastindex = {}
        for i,v in enumerate(s):
            lastindex[v] = i
        
        # find the partition
        res = []
        size = 0 # partition_size
        end = 0 # partition_end
        for i,v in enumerate(s):
            size += 1
            end = max(end, lastindex[v])
            if i == end: # end of the partition
                res.append(size)
                size = 0 # restart the partition
        return res