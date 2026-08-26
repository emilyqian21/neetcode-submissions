class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern2wrd = {}
        for s in strs:
            pattern = [0] * 26
            for c in s:
                pattern[ord(c) - ord('a')] += 1
            pattern = tuple(pattern)
            if pattern not in pattern2wrd:
                pattern2wrd[pattern] = []
            pattern2wrd[pattern].append(s)
        
        res = []
        for v in pattern2wrd.values():
            res.append(v)
        return res