"""
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
import unittest


class Solution:
    def searchMatrix(self, matrix, target):
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로
            elif target > matrix[row][col]:
                row += 1
        return False

    def searchMatrix_pythonic(self, matrix, target):
        return any(target in row for row in matrix)


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
            3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 5
        self.assertTrue(s.searchMatrix(matrix, target))
        self.assertTrue(s.searchMatrix_pythonic(matrix, target))

        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
            3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 20
        self.assertFalse(s.searchMatrix(matrix, target))
        self.assertFalse(s.searchMatrix_pythonic(matrix, target))


if __name__ == "__main__":
    unittest.main()
