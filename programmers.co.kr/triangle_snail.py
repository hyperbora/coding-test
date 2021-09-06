"""
https://programmers.co.kr/learn/courses/30/lessons/68645
삼각 달팽이
(0,0)에서 시작해서 반시계방향으로 삼각형을 채워서 해당 1차원 리스트를 리턴합니다.
"""
from typing import List
from itertools import chain
import unittest


def solution(n):
    answer: List[List[int]] = [[0] * (i + 1) for i in range(n)]

    dx: tuple[int] = (1, 0, -1)
    dy: tuple[int] = (0, 1, -1)
    direction: int = 0

    cur_x = 0
    cur_y = 0
    answer[0][0] = 1
    num = 1
    last = n * (n + 1) // 2
    while num < last:
        next_x = cur_x + dx[direction]
        next_y = cur_y + dy[direction]
        if 0 <= next_x < n and 0 <= next_y < len(answer[next_x]) and answer[next_x][next_y] == 0:
            num += 1
            answer[next_x][next_y] = num
            cur_x, cur_y = next_x, next_y
        else:
            direction = (direction + 1) % len(dx)

    return list(chain.from_iterable(answer))


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(4), [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
        self.assertListEqual(
            solution(5), [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
        self.assertListEqual(solution(
            6), [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])


if __name__ == "__main__":
    unittest.main()
