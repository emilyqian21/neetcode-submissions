class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)

        s1_count = {}
        window = {}

        # build counts
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        for c in s2[:k]:
            window[c] = window.get(c, 0) + 1

        # number of chars whose frequencies match
        match = 0
        for c in s1_count:
            if window.get(c, 0) == s1_count[c]:
                match += 1
        # TEST initial window
        if match == len(s1_count):
                return True
        l = 0

        for r in range(k, len(s2)):
            # add right character
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            if c in s1_count:
                if window[c] == s1_count[c]:
                    match += 1
                elif window[c] == s1_count[c] + 1:
                    match -= 1

            # remove left character
            c = s2[l]
            window[c] -= 1

            if c in s1_count:
                if window[c] == s1_count[c]:
                    match += 1
                elif window[c] == s1_count[c] - 1:
                    match -= 1
            # test the new window
            if match == len(s1_count):
                return True
            l += 1

        return match == len(s1_count)