class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [i for i in range(len(nums))]
        for i in range(len(nums)):
            result[i] = nums[i]**2
        return sorted(result)