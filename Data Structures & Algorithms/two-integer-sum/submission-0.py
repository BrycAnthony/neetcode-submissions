class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in pair:
                return [pair[needed], i]
            pair[num] = i