"""
https://programmers.co.kr/learn/courses/30/lessons/12905
가장 큰 정사각형 찾기
"""
from typing import List
import unittest


def solution(board: List[List[int]]) -> int:
    answer: int = 0
    matrix: List[List[int]] = [[0] * (len(board[0]) + 1)
                               for _ in range(len(board) + 1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            matrix[i + 1][j + 1] = board[i][j]

    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            if matrix[i][j] != 0:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i]
                                   [j - 1], matrix[i - 1][j - 1]) + 1
                answer = max(answer, matrix[i][j])

    return answer ** 2


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(
            solution(board=[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]), 9)
        self.assertEqual(solution(board=[[0, 0, 1, 1], [1, 1, 1, 1]]), 4)


if __name__ == "__main__":
    unittest.main()
