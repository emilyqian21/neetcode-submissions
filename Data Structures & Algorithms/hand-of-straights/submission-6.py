class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # time: O(nlogn)
        # space: O(n)
        # main logic:
            # 1) 每次都必须从当前最小的、还没被用完的牌开始组 consecutive group。
            #    为什么？因为最小的牌没有更小的牌能来“配它”，所以它如果不能作为某一组的开头，就永远没地方去了。
            # 2_ 当前最小剩余牌必须开组；它有几张，就一次开几组

        #edge case 
        if len(hand) % groupSize != 0:
            return False

        count = {} # {number : frequency}
        for n in hand:
            count[n] = count.get(n,0) + 1
        
        sorted_count = sorted(count) # 等同于sorted(count.keys()) ,就是一个list 
        # 如果要sort by value , reverse
        # sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        # 比如： count = {3: 2, 1: 5, 2: 1}, sorted_count = [1, 2, 3]

        for n in sorted_count:
            if count[n] > 0: 
                first = n
                first_freq = count[n] 

                for next_n in range(first, first + groupSize):
                    # check if available
                    if count.get(next_n, 0) < first_freq: # If the smallest number appears k times,we need k copies of every number.
                        return False
                    else:
                        count[next_n] -= first_freq
                # end of current group starting with n, continue next group with next iteration in count
        return True

    