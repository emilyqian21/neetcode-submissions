class Twitter:
# time: O(FlogF) F = num of followees
# space: O(F) heap中只先存每个关注用户的最近的一条feed,所以是 F = num of followees
#For postTweet, it's O(1) because we only keep the latest 10 tweets per user.
#For getNewsFeed, we use k-way merge. We initialize the heap with one tweet from each followee, which costs O(F log F), and then retrieve at most 10 tweets, which costs O(log F). Therefore the overall complexity is O(F log F). The heap stores at most F tweets, so the space complexity is O(F).
    def __init__(self):
        self.account_followed = defaultdict(set)
        self.account_to_posts = defaultdict(list)
        self.post_order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.account_to_posts[userId].append((self.post_order,tweetId))
        # optimize space
        while len(self.account_to_posts[userId]) > 10:
            self.account_to_posts[userId].pop(0) #list.pop()是删除最后的即最右边的
        self.post_order -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        # 把自己的feed也放进去（把自己的账号算进去）
        self.account_followed[userId].add(userId)

        # for 每个关注的账号（包括自己的）：
        for followed_acc in self.account_followed[userId]:
            # 如果这个account发过po
            if followed_acc in self.account_to_posts:
                index = len(self.account_to_posts[followed_acc]) - 1 # 这个account发的最后一条twitter
                po, tid = self.account_to_posts[followed_acc][index] # 最后一条twitter的时间和twitter_id
                heapq.heappush(heap, (po, tid, followed_acc, index -1)) # (发布时间，tid, 发的账号， 上一条的index)

        while heap and len(res) < 10: # 一直加和pop，直到re能到达10条
            po, tid, followed_acc, index = heapq.heappop(heap) # 最小的po被pop,就是最晚加进去的 -8
            res.append(tid)
            if index >= 0: # 这个account还有其他feed的话
                po, tid = self.account_to_posts[followed_acc][index] # 把这个account的上一条也加进heap
                heapq.heappush(heap, (po, tid, followed_acc, index -1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # self.account_to_fans[followeeId].add(followerId)
        if followerId != followeeId:
            self.account_followed[followerId].add(followeeId)
            return


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if follwerId in self.account_to_fans[followeeId]:
        #     self.account_to_fans[followeeId].remove(follwerId)
        # return
        if followeeId in self.account_followed[followerId]:
            self.account_followed[followerId].remove(followeeId)
        return