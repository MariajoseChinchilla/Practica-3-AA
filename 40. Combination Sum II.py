class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def recursive(current, pos, target):
            if target == 0:
                res.append(current.copy())
            if target <= 0:
                return

            p = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == p:
                    continue
                current.append(candidates[i])
                recursive(current, i + 1, target - candidates[i])
                current.pop()
                p = candidates[i]

        recursive([], 0, target)
        return res