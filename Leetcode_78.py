class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = []
        def dfs(index, path):
            res.append(prev[:])
            if len(path) == len(nums):
                return
            for e in range(index, len(nums)):
                prev.append(nums[e])
                dfs(e + 1, path + [nums[e]])
                prev.pop()
        dfs(0,[])
        return res