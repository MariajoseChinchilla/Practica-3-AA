class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        curRow, nextRow = triangle[N - 2], triangle[N - 1]

        for i in range(N - 2, -1, -1):
            for j in range(i + 1):
                curRow[j] += min(nextRow[j], nextRow[j + 1])

            nextRow = curRow
            curRow = triangle[i - 1]

        return nextRow[0]