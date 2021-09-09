"""
https://programmers.co.kr/learn/courses/30/lessons/49994
방문 길이
경계를 넘어가지 않으면서 최고 방문한 길의 길이를 리턴
"""

from typing import Dict, Set, Tuple
import unittest


def solution(dirs) -> int:
    answer: int = 0
    # up, down, left, right
    dx: Tuple[int] = (0, 0, -1, 1)
    dy: Tuple[int] = (1, -1, 0, 0)
    s: Set = set()
    current_x: int = 0
    current_y: int = 0
    direction: Dict = {"U": 0, "D": 1, "L": 2, "R": 3}
    for path in dirs:
        next_x: int = current_x + dx[direction[path]]
        next_y: int = current_y + dy[direction[path]]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            left_to_right: Tuple = (current_x, current_y, next_x, next_y)
            right_to_left: Tuple = (next_x, next_y, current_x, current_y)
            if left_to_right not in s and right_to_left not in s:
                s.add(left_to_right)
                s.add(right_to_left)
                answer += 1
            current_x, current_y = next_x, next_y
    return answer


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(dirs="ULURRDLLU"), 7)
        self.assertEqual(solution(dirs="LULLLLLLU"), 7)


if __name__ == "__main__":
    unittest.main()
