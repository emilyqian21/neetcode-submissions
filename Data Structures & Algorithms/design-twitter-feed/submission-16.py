class Twitter:

    def __init__(self):
        self.posts = {} # key = userid, val = [(time, tweetid)]
        self.following = {} # key = userid, val = set(following accounts) 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # get follower list
        followinglist = {userId} # set
    
        if userId in self.following:
            followinglist.update(self.following[userId])
        
        heap = [] # we need the latest, so maxheap, always pop the largest time value twitter
        # get the latest tweet from every user
        for user in followinglist:
            if user in self.posts:
                idx = len(self.posts[user]) - 1 # the index for the last twitter
                time, twitter = self.posts[user][idx]
                heapq.heappush(heap, (-time, user, twitter, idx))

        # start to collect the 10 latest twitter
        res = []
        while heap and len(res) < 10:
            neg_time, user, twitter, idx = heapq.heappop(heap)
            res.append(twitter)

            # add back if there's twitter remaining for this user
            if idx > 0:
                idx = idx - 1 # the next latest twitter idx
                time, twitter = self.posts[user][idx]
                heapq.heappush(heap, (-time, user, twitter, idx))
                
        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
