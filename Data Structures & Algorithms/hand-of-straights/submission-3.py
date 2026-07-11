class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #edge case 
        if len(hand) % groupSize != 0:
            return False

        count = {} # {number : frequency}
        for n in hand:
            count[n] = count.get(n,0) + 1
        
        sorted_count = sorted(count) # 等同于sorted(count.keys()) ,就是一个list
        # 如果要sort by value , reverse
        # sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        for n in sorted_count:
            if count[n] > 0: 
                first = n
                first_freq = count[n]

                for next_n in range(first, first + groupSize):
                    # check if available
                    if count.get(next_n, 0) < first_freq:
                        return False
                    else:
                        count[next_n] -= first_freq
                # end of current group starting with n, continue next group with next iteration in count
        return True

    