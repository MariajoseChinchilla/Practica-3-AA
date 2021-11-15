import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 1:
            return log2(n) - int(log2(n)) == 0
        elif n == 1:
            return True 