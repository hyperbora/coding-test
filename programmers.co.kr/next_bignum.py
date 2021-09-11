"""
https://programmers.co.kr/learn/courses/30/lessons/12911
다음 큰 숫자
"""
import unittest


def solution(n: int) -> int:
    count = bin(n).count('1')
    n = n + 1
    while True:
        if bin(n).count('1') == count:
            return n
        n += 1


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(n=78), 83)
        self.assertEqual(solution(n=15), 23)


if __name__ == "__main__":
    unittest.main()
