class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        N = len(nums)
        st, end = -1, -1
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        if l < N and nums[l]== target:
            st = l
        if nums[r-1] == target:
            end = r - 1
        return [st,end]