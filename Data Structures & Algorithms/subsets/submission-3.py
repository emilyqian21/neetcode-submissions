class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        def dfs(start):
            res.append(path.copy()) # 记录答案

            for i in range(start, len(nums)):
                path.append(nums[i]) #做选择
                dfs(i + 1) #继续探索：在当前path基础上，只能从 i+1 之后的元素继续扩展组合
                # 以当前 path + nums[i] 作为前缀的所有扩展分支已经探索完了
                path.pop()  # 撤销选择，回到分叉点： 撤销刚刚添加的nums[i],回到for loop, 继续尝试下一个 i

        dfs(0)
        return res
        # Time: O(n · 2ⁿ)
        # Space (excluding output): O(n)
        # Output size: O(n · 2ⁿ)

        #mental model
        # def dfs(start):
            # record_answer_if_needed()

            # for choice in available_choices:
            #     choose
            #     dfs(next_state)
            #     unchoose
    
    #mental model

    # def dfs(state):

    # # 1. Record answer if current node is a solution
    # if is_solution(state):
    #     record_answer()

    # # 2. Generate possible choices
    # for choice in choices(state):

    #     # 3. Prune bad/redundant choices
    #     if should_prune(choice, state):
    #         continue

    #     # 4. Make choice
    #     make_choice(choice)

    #     # 5. Explore
    #     dfs(next_state)

    #     # 6. Undo choice
    #     undo_choice(choice)