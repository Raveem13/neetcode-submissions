class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = act = 0
        for n in nums:
            res ^= n
        for i in range(len(nums)+1):
            act ^= i
        return res^act