class Solution:
    def firstBadVersion(self, n):
        l, r = 0, n
        while l < r:
            mid = int((l+r)/2)
            if isBadVersion(mid):
                r = mid
            else:
                l= mid + 1
        return l