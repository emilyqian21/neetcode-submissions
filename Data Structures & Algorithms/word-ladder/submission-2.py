class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # time: O ( m ^2 * n) m = length of words, n = number of words
        # space:  O ( m ^2 * n)
        if endWord not in wordList:
            return 0 
        pattern2nei = collections.defaultdict(list)
        wordList.append(beginWord) # add beginword into the wordList
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                pattern2nei[pattern].append(word)
        visit = set()

        q = deque([beginWord])
        visit.add(beginWord)
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in pattern2nei[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
                pattern2nei[pattern] = []
            # end of this level traversal
            res += 1
        return 0

