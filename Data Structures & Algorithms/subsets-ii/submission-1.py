class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start,path):
            #record answer ： 什么时候储存答案？ --> 任何节点都要存，permutation是需要path == len(nums)再存
            res.append(path.copy())
            #Subset：当前节点虽然已经是答案，但还不是叶子节点，后面还有子集要继续探索，所以绝对不能 return。
            #Permutation：到叶子节点了，已经没有事情可做，return 只是提前结束，不写也对。
            
            # explore all start options
            for i in range(start,len(nums)):
                
                #跳过重复的
                if i > start and nums[i] == nums[i - 1]:
                    continue
                #current node
                path.append(nums[i])
                #explore further options based on this path
                dfs(i+1, path) # can't reuse the current start

                # cancel 
                path.pop()
        
        dfs(0,[])
        return res
        #time: O(n*2^n) 一共有2^n个subset，copy()需要花 O(n)，所以一共是 O（n*2^n)
        #space: 不算返回结果，o(n)，因为stack是n， 算返回结果是O（n*2^n)