class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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
                while l < r:
                    m = (l + r)//2
                    if lst[m] < num:
                        l = m + 1
                    else:
                        r = m 
                lst[l] = num
        return max_len
