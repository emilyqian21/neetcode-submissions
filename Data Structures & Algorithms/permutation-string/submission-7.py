class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 用need, have

        if len(s1) > len(s2):
            return False

        count_s1 = collections.Counter(s1)
        count_s2 = collections.Counter(s2[:len(s1)])

        need = len(count_s1)
        have = 0

        # initialize have
        for c in count_s1:
            if count_s1[c] == count_s2[c]:
                have += 1

        if have == need:
            return True

        l = 0

        for r in range(len(s1), len(s2)):

            # add right
            c1 = s2[r]
            count_s2[c1] = count_s2.get(c1, 0) + 1

            if c1 in count_s1:
                if count_s2[c1] == count_s1[c1]:
                    have += 1
                elif count_s2[c1] == count_s1[c1] + 1:
                    have -= 1


            # remove left
            c2 = s2[l]
            count_s2[c2] -= 1

            if c2 in count_s1:
                if count_s2[c2] == count_s1[c2]:
                    have += 1
                elif count_s2[c2] == count_s1[c2] - 1:
                    have -= 1

            

            if have == need:
                return True

            l += 1

        return False