class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in visited:
                return [visited[complement]+1,i+1]
            visited[numbers[i]] = i 
            