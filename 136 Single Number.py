class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = set(nums)
        for i in numbers:
            nums.remove(i)
        for num in numbers:
            if num not in nums:
                return num