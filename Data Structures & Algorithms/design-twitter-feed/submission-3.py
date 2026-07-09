class Twitter:

    def __init__(self):
        # self.account_to_fans = defaultlist(set)
        self.account_followed = defaultdict(set)
        self.account_to_posts = defaultdict(set)
        self.post_order = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.account_to_posts[userId].add((tweetId,self.post_order))
        self.post_order -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followed_acc in self.account_followed[userId]:
            for tid, po in self.account_to_posts[followed_acc]:
                heapq.heappush(heap, (po,tid))
        for tid,po in self.account_to_posts[userId]:
            heapq.heappush(heap,(po,tid))

        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
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