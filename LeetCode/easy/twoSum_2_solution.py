class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, key in enumerate(nums):

            if target - key in d:
                return [i, d[target - key]]
            else:
                d[key] = i