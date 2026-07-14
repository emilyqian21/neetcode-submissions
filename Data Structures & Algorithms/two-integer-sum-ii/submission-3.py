class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # pattern: sorted array, find pair
        # solution: two pointers

        # time: O(n)
        # space: O(1)

        l = 0
        r = len(numbers)-1

        while l < r: # can't be <= because index can only be used once
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
            