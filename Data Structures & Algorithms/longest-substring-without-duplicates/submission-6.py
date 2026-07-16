class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)

            seen[s[r]] = r
            ans = max(ans, r - l + 1)

        return ans