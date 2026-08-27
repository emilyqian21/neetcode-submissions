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
                # do i need to update maxfreq? --> will counter[s[l]] affect mamxfreq? --> "bbacb"k = 1
            res = max(res, r - l + 1)
        return res
