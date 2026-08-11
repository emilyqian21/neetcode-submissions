class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # time: O(n)
        # space: O(n)
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False