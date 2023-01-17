class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # list
        # pair = []
        # sum = 0
        # nums.sort()
        # for i in nums:
        #     pair.append(i)
        #     if len(pair) == 2:
        #         sum += min(pair)
        #         pair = []
        # return sum
    
        # enumerate
        nums.sort()
        sum = 0
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum
        
        # pythonic
        # return sum(sorted(nums)[::2])