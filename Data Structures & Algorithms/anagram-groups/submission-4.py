class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            pattern = [0]*26
            for c in s:
                pattern[ord(c)- ord('a')] += 1
            res[tuple(pattern)].append(s)
        
        return list(res.values())