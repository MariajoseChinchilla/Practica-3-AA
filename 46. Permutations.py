from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations([i for i in nums])