class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 记这个吧
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # initialize first fixed window
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # count = how many of the 26 chars currently have matching frequency
        need = 26
        have = 0
        for i in range(26):
            if count1[i] == count2[i]:
                have += 1

        l = 0

        for r in range(len(s1), len(s2)):
            if have == 26:
                return True

            # add right char
            idx = ord(s2[r]) - ord('a')
            count2[idx] += 1

            if count2[idx] == count1[idx]:
                have += 1
            elif count2[idx] == count1[idx] + 1:
                have -= 1

            # remove left char
            idx = ord(s2[l]) - ord('a')
            count2[idx] -= 1

            if count2[idx] == count1[idx]:
                have += 1
            elif count2[idx] == count1[idx] - 1:
                have -= 1

            l += 1

        return have == 26