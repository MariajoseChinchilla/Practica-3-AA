class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        p = 1
        mini = 0
        subarrays = 0
        total = 0

        for i in range(N):
            p *= nums[i]
            subarrays += 1

            while p >= k and mini <= i:
                p /= nums[mini]
                mini += 1
                subarrays -= 1

            if p < k:
                total += subarrays
        return total