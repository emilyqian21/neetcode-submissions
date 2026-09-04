class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # N = number of words
        # M = word length
        # time: O(N * M^2)
        # space: O(N * M^2)

        if endWord not in wordList:
            return 0

        pattern2nei = collections.defaultdict(list)

        # 避免修改传入的 wordList
        words = wordList + [beginWord]

        for word in words:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                pattern2nei[pattern].append(word)

        visited = {beginWord}
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for neighbor in pattern2nei[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

                    # 必须在 for j 里面：
                    # 当前 pattern 的所有 neighbor 都已被发现
                    pattern2nei[pattern] = []

            res += 1

        return 0

