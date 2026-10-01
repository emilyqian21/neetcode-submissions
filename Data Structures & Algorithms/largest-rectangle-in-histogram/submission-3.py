class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # main logic: 
        # 用一个 monotonic increasing stack 来 存还没有遇到右边界的柱子。
        # 每个元素存 (start_index, height)：
                # - start_index：这个高度最早可以从哪个 index 开始
                # - height：这个矩形的高度

        # step 1: 遇到更矮的柱子 → 把前面更高的柱子结算掉；同时让当前矮柱子尽量往左延伸。
            #  stack 里存的是“还可以继续往右延伸的柱子”。
            #  一旦遇到更矮的柱子，就说明前面比它高的柱子不能再往右延伸了，要立刻算面积。
            #  结算完面积后，高柱子的起始位置可以让低柱子继承，因为低柱子肯定能往左延伸。

        # step 2: 最后 stack 里剩下的柱子，说明右边一直没遇到更矮的，所以它们都可以一路延伸到数组末尾。
        
        stack = []  # (start_index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start_index = i # 这个高度最早可以从自己的位置i开始

            while stack and stack[-1][1] > height: # 如果有stack, 且stack里上一个柱子的高度高于现在的柱子；那上一个柱子不能往右延伸了，需要结算掉
                prev_start, prev_height = stack.pop()

                width = i - prev_start
                max_area = max(max_area, width * prev_height)

                
                start_index = prev_start # 继承上一个柱子的起始位置 # current shorter bar can extend back to the popped bar's start index

            stack.append((start_index, height))

        # bars left in stack can extend to the end
        for start_index, height in stack:
            width = len(heights) - start_index
            max_area = max(max_area, width * height)

        return max_area