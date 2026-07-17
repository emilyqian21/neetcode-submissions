class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # 用monotonic decreasing queue 
    # time: O(n)
    # space: O(n)
        l = 0 # windows 最左侧 
        r = 0  # windows 最右侧
        res = []
        q = deque() # 存可能的candidate 的 index
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # q最右侧的代表的值 比 r代表的值小，那q最右侧的代表值 肯定不会是答案了，扔掉
                q.pop()
            q.append(r) # r 可能是答案。经过这一番pop, 比r小的都已经删光了，只有比r大的在r左侧

            #检查q是否valid 
            if l > q[0]: # 如果q[0]，也就是最早加入且有可能的candidate，假设已经在边界外了，我们就可以把它扔掉
                q.popleft()
            
            #检查windows 且记录答案
            if r + 1 >= k: # windows已经足够长了，比如之前是1,2，现在终于够长度3了，之后都是需要进一个，扔一个了
                #windows长度valid， 可以记录答案
                res.append(nums[q[0]]) # 不能pop 因为这个数字可能是好几个windows的答案
                l += 1
            r += 1
        return res