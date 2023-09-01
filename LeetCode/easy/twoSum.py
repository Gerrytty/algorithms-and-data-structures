class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            if num in d:
                d[num].append(i)
            else:
                d[num] = [i]

        for key in d:

            key2 = None

            if key <= abs(target) and (target - key) in d:
                key2 = target - key

            if key2 is not None:

                if key == key2 and len(d[key]) > 1:
                    return [d[key][0], d[key][1]]
                elif key != key2:
                    return [d[key][0], d[key2][0]]