class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # time: O(nlogn)
        # space: O(n)
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        heap = list(count.keys()) # store the unique values, rank by value
        heapq.heapify(heap)

        while heap:
            first_val = heap[0]
            for i in range(first_val, first_val + groupSize): # build the group
                if i not in count: # if such value doesn't exist in our hand
                    return False
                count[i] -= 1 # decrement the count for the i
                if count[i] == 0: # if used all i and it's not the minimal value, then there will be holes
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True