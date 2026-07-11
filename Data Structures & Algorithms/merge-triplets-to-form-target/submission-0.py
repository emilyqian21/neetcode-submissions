class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # time: O(n)
        # space: O(1)
        # 如果triplet里的某个数 > target里的同个位置的数 --> 这个triplet不能用
        # 如果能用的triplet里的某个数 和target里的同个位置的数一样---> target里这个位置的数是可以找到的
        achievable = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            else:
                for i, v in enumerate(t): # 0, v; 1,v; 2,v
                    if t[i] == target[i]:
                        achievable.add(i) # 存 i, 说明target[i]已经能完成任务了
        return len(achievable) == 3
        
