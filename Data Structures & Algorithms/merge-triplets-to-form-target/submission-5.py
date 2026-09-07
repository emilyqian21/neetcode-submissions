class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # time: O(n)
        # space: O(1)
        # main logic: 
        # 因为merge的时候， 每个位置只会越来越大，不会变小
        # 所以超过target[i]的t[i]肯定不能用，那个triplet就得跳过
        # 所以先删掉任何超过 target 的 triplet；
        # 剩下的 triplet 只要能 collectively hit target 的 3 个 coordinates，就可以 merge 出 target。 
        
        achievable = set()

        for t in triplets:
            # This triplet can never be used,
            # because merge only takes max and cannot decrease later.
            if (
                t[0] > target[0]
                or t[1] > target[1]
                or t[2] > target[2]
            ):
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    achievable.add(i)

        return len(achievable) == 3