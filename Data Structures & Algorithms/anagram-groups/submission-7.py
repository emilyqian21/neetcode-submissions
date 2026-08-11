class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern2word = defaultdict(list)

        for s in strs:
            pattern = [0]*26 # for 26 letters
            for c in s:
                pattern[ ord(c) - ord("a")] += 1
            
            pattern2word[tuple(pattern)].append(s)
        res = []
        for k,v in pattern2word.items():
            res.append(v)
        return res