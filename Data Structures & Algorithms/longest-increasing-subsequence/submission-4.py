class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time: O(nlogn) You process each number once (n iterations). For each number, you perform a binary search on lst (log n in the worst case).
        # space: O(n)
        # if larger than the last digit in lst, max_len += 1
        # else, replace the value in the lst 
        lst = [nums[0]]
        max_len = 1

        for num in nums[1:]:
            if num > lst[-1]:
                max_len += 1
                lst.append(num)
            else: # binary search on lst
                l,r = 0,len(lst) - 1
                while l < r: # template for finding the first index that's equal or larger than the num
                    m = (l + r)//2
                    if lst[m] < num:
                        l = m + 1
                    else:
                        r = m 
                lst[l] = num # index of the first element in lst that is greater than or equal to num
        return max_len
