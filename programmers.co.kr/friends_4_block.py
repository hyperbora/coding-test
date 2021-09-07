"""
https://programmers.co.kr/learn/courses/30/lessons/17679
[1차] 프렌즈4블록
"""

from typing import List
import unittest


def solution(m: int, n: int, board: List[str]) -> int:
    board = [list(x) for x in board]

    matched: List[List[int]] = [[0]]
    while matched:
        # 1) 일치 여부 판별
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j + 1] == board[i + 1][j] != '#':
                    matched.append([i, j])

        # 2) 일치한 위치 삭제
        for i, j in matched:
            board[i][j] = board[i][j + 1] = \
                board[i + 1][j + 1] = board[i + 1][j] = '#'

        # 3) 빈공간 블럭 처리
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'
    return sum(x.count('#') for x in board)


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(
            solution(m=4, n=5, board=["CCBDE", "AAADE", "AAABF", "CCBBF"]), 14)
        self.assertEqual(solution(m=6, n=6, board=[
                         "TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]),	15)


if __name__ == "__main__":
    unittest.main()
