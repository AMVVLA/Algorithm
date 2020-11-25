class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}
        for i, num in enumerate(nums):
            if target - num in nums_dic:
                return [nums_dic[target - num], i]
            nums_dic[num] = i