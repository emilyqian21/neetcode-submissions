class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key = lambda x: x[0])
        output = []

        for interval in intervals:
            if output and interval[0] <= output[-1][1]: # s2 <= e1, overlap
                output[-1] = [min(interval[0], output[-1][0]),max(interval[1], output[-1][1])]
            else:
                output.append(interval)
        return output
