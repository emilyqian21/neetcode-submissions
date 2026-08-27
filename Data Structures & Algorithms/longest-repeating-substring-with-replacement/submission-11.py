class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # len of the string - the most frequent character frequench <= k is valid

        res = 0
        counter = {}
        maxfreq = 0
        l = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxfreq = max(maxfreq, counter[s[r]])

            if (r - l + 1) - maxfreq > k: # invalid
                # srhink
                
                counter[s[l]] -= 1
                l += 1
                # do i need to update maxfreq? --> will counter[s[l]] affect mamxfreq? --》无所谓，就算maxfreq stale也无所谓，因为我们只在乎最大的window size. (r - l + 1) 必须<= k + maxfreq, 如果（r- l + 1）要增加，就必须maxfreq增加，maxfreq增加就只可能是通过r traverse的新character增加
            res = max(res, r - l + 1)
        return res
