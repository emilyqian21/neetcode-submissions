class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Time: O(n)
        # Space: O(1) extra space
        
        #从右往左：< 9 就 +1 然后 return；== 9 就变成 0，继续 carry。
        # Start from the last digit.
        # If digit < 9, add 1 and finish.
        # If digit == 9, it becomes 0 and carry continues left.

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        # If every digit was 9:
        # [9,9,9] -> [1,0,0,0]
        return [1] + digits