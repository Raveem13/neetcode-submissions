class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dif = len(nums)
        for i in range(len(nums)):
            dif += i - nums[i]
        return dif 