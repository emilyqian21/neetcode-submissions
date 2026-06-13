class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for string in strs:
            pattern = [0]*26
            for i in range(len(string)):
                #save pattern for each string 
                pattern[ ord(string[i]) - ord('a')]+= 1
            pattern_key = tuple(pattern)
            dic[pattern_key].append(string)
        res = []
        for key in dic:
            res.append(dic[key])
        return res