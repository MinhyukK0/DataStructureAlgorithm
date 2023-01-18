class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = post = 1
        sol = []
        for i in range(len(nums)):
            sol.append(pre)
            pre = pre * nums[i]
        for i in range(len(nums)-1, -1, -1):
            sol[i] *= post
            post = post * nums[i]
        return sol