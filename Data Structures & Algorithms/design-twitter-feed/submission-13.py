class Twitter:

    def __init__(self):
        self.account2fans = defaultdict(set)
        self.account2follow = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1 # b/c we need to use maxheap, so the latest will have the smallest value

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        followlist = self.account2follow[userId]
        followlist.add(userId)
        # 1. save all the latest tweets from the writers
        for writer in followlist:
            alltweets = self.tweets[writer]
            if alltweets:
                index = len(alltweets) -1
                lasttweet = alltweets[index]
                lasttweet_time, lasttweet_id = lasttweet[0], lasttweet[1]
                heap.append([lasttweet_time, lasttweet_id, writer, index -1]) # the next available latest tweet index
        # 2. heapify the res, order by lasttweet_time
        heapq.heapify(heap)
        # 3. pop
        while len(res) < 10 and heap:
            lasttweet_time, lasttweet_id, writer, new_index = heapq.heappop(heap)
            res.append(lasttweet_id)

            # add the next one
            alltweets = self.tweets[writer]
            if alltweets and new_index < len(alltweets) and new_index >= 0:
                lasttweet = alltweets[new_index]
                lasttweet_time, lasttweet_id = lasttweet[0], lasttweet[1]
                heapq.heappush(heap, [lasttweet_time, lasttweet_id, writer, new_index -1])
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.account2fans[followeeId].add(followerId)
        self.account2follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.account2fans[followeeId]:
            self.account2fans[followeeId].remove(followerId)
        if followeeId in self.account2follow[followerId]:
            self.account2follow[followerId].remove(followeeId)