class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use XOR --> SAME ELEMENT WILL CANCEL OUT TO 0
        # a ^ a = 0
        # a ^ 0 = a
        # the one that is not zero is single number

        # XOR fundamentally works on bits / integers, not directly on Python strings!!
        # 'a' ^ 'b'   # TypeError
        # need to convert to numbers --> ord('a') ^ ord('b')

        res = 0
        for n in nums:
            res ^=n
        return res