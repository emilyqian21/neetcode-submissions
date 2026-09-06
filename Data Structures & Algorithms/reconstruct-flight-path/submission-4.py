class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Pattern: Eulerian Path
        # 题目要求每张 ticket（edge）都 exactly once。
        #
        # 核心：
        # 1. 当前机场还有 ticket -> 继续往前飞，push 到 stack
        # 2. 当前机场已经没 ticket -> 它应该放到当前剩余路线的最后面
        #    所以从 stack pop 出来，放进 itinerary
        # 3. itinerary 是从“最后一个机场”开始收集的，所以最后 reverse
        #
        # Time: O(E log E)
        # Space: O(E + V)

        graph = defaultdict(list)

        # graph[src] = 从 src 还能飞去的所有 destination
        for src, dst in tickets:
            graph[src].append(dst)

        # 我们之后用 list.pop()，它会拿最右边的元素。
        # 所以先 reverse sort，让字典序最小的机场放在最右边。因为题目要求 return the lexicographically smallest one.
        #
        # example:
        # JFK -> ["HOU", "SEA"]
        # reverse sort -> ["SEA", "HOU"]
        # pop() -> "HOU"  (lexical smallest)
        for src in graph:
            graph[src].sort(reverse=True)

        # stack = 当前正在走、但位置还没有最终确定的路线
        stack = ["JFK"]

        # itinerary = 已经确定位置的机场
        # 注意：我们是从路线末尾开始确定，所以这里存的是反向答案
        itinerary = []

        # 只要 stack 里还有机场没最终处理完，就继续
        while stack:

            # stack[-1] = 当前所在机场
            # graph[stack[-1]] = 当前机场还剩哪些 unused tickets
            #
            # 只要当前机场还能飞，就一直往前走
            while graph[stack[-1]]:
                next_airport = graph[stack[-1]].pop()
                stack.append(next_airport)

            # 走到当前机场已经没有 unused ticket 了：
            # 这个机场就是“当前剩余路线的最后一个机场”
            # 所以把它从 stack 拿出来，加入反向答案
            itinerary.append(stack.pop())

        # itinerary 是从后往前构造的，所以 reverse
        return itinerary[::-1]