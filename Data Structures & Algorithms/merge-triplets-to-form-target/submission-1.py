class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if the value in triplet is larger than that in target, this triplet can't be the answer
        achievable = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            else:
                for i,v in enumerate(t):
                    if v == target[i]:
                        achievable.add(v)
        return len(achievable) == len(set(target))