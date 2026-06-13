class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            pattern = [0]*26
            for c in s:
                pattern[ord(c)- ord('a')] += 1
            res[tuple(pattern)].append(s)
        
        return list(res.values()) #必须用list()!!!, 因为res.values() 是一个object
        #time: O(M*N) m is num of strings , n is length of longest string
        #space: O(M*N)