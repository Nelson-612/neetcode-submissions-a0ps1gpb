class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows*cols - 1

        while left <= right:
            mid = (right + left) // 2
            midVal = matrix[mid//cols][mid%cols]
            if midVal == target:
                return True
            elif midVal < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
