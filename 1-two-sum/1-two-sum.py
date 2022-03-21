class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}
        for idx, num in enumerate(nums):
            res_num = target-num
            if res_num in res_dict:
                return [res_dict[res_num], idx]
            res_dict[num] = idx