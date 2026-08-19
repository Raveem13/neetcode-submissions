class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, val in enumerate(nums):
            if (target - val) in hashMap:
                return [hashMap[target - val], i] 
            hashMap[val] = i