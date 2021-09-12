"""
https://programmers.co.kr/learn/courses/30/lessons/12913
땅따먹기
"""
from typing import List
import unittest


def solution(land: List[List[int]]) -> int:
    length: int = len(land)

    for i in range(1, length):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    return max(land[length-1])


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(
            solution(land=[
                [1, 2, 3, 5],
                [5, 6, 7, 8],
                [4, 3, 2, 1]
            ]
            ), 16)


if __name__ == "__main__":
    unittest.main()
