class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer
        l = 0
        r = len(numbers) -1 

        while l<r:
            total_sum = numbers[l] + numbers[r]
            if total_sum == target:
                return [l+1, r+1]
            elif total_sum < target:
                l += 1
            else:
                r -= 1
        





        # # hashset solution 
        # visited = {}
        # for i in range(len(numbers)):
        #     complement = target - numbers[i]
        #     if complement in visited:
        #         return [visited[complement]+1,i+1] #因为一定是先看到complement,再看到现在的i
        #     visited[numbers[i]] = i 
        # #time: O(N)
        # #space: O(N)


            