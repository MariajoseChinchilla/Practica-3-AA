from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = set(permutations(nums))
        return [i for i in perm]