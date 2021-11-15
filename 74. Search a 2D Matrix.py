class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        margins = []
        for i in range(rows):
            margins.append(matrix[i][cols-1])
        for num in margins:
            if target <= num:
                if target in matrix[margins.index(num)]:
                    return True
                break
        return False