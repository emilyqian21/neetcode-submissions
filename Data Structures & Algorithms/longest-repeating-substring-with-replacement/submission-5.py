class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #different characters as valid condition?
        # 窗口合法的condition： 除去frequncy最多的字符外，剩下的字符数量 < K
        l = 0
        freq = {}
        max_freq = 0 
        max_res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            max_freq = max(max_freq, freq[s[r]]) #这样不用每次都计算max freq是什么了

            while freq and (r - l + 1) - max_freq > k: # 剩下的非最多的数字>k个，需要shrink，直到合法为止
                freq[s[l]] = freq.get(s[l],0) - 1
                l += 1
            length = r - l + 1
            max_res = max(max_res, length)

        return max_res
