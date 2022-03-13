class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = []

        def dfs(my_list: List[int]):
            if not my_list:
                res.append(prev[:])
            for i in my_list:
                nex = my_list[:]
                nex.remove(i)
                prev.append(i)
                dfs(nex)
                prev.pop()

        dfs(nums)
        return res
