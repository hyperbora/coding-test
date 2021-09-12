"""
https://programmers.co.kr/learn/courses/30/lessons/12949
행렬의 곱셈
"""

from typing import List
import unittest


def solution(arr1, arr2) -> List[List[int]]:
    answer: List[List[int]] = []
    for i in range(0, len(arr1)):
        temp: List[int] = []
        for j in range(0, len(arr2[0])):
            s: int = 0
            for k in range(0, len(arr1[0])):
                s += arr1[i][k] * arr2[k][j]
            temp.append(s)
        answer.append(temp)

    return answer


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(arr1=[[1, 4], [3, 2], [4, 1]], arr2=[
                             [3, 3], [3, 3]]), [[15, 15], [15, 15], [15, 15]])
        self.assertListEqual(solution(arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]], arr2=[
                             [5, 4, 3], [2, 4, 1], [3, 1, 1]]), [[22, 22, 11], [36, 28, 18], [29, 20, 14]])


if __name__ == "__main__":
    unittest.main()
