class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 能走就 push，走不动就 pop 到答案；最后 reverse。
        # stack记录目前的路程，itinary记录死路 （所以最后是reverse一下）
        # time: O(E log E)
        # space: O(E + V)
        graph = defaultdict(list)

        # build graph
        for src, dst in tickets:
            graph[src].append(dst)

        # reverse sort so pop() gets lexical smallest
        for src in graph:
            graph[src].sort(reverse=True)

        stack = ["JFK"]
        itinerary = []

        while stack:
            # 还有 ticket，就继续走
            while graph[stack[-1]]:
                next_airport = graph[stack[-1]].pop()
                stack.append(next_airport)

            # 死路：这个 airport 的位置可以确定
            itinerary.append(stack.pop())

        return itinerary[::-1]


        # 1. ticket 是 edge
        #    → 每条 edge 必须 exactly once
        #    → Eulerian Path

        # 2. 能走就一直走
        #    → 用 stack 记录当前走过的路线

        # 3. 走到死路
        #    → 这个机场可以确定了
        #    → stack.pop() 放进 itinerary

        # 但是：
        #    最先确定的是最后一个机场
        #    → itinerary 是倒着构造的
        #    → 最后 reverse