"""
https://programmers.co.kr/learn/courses/30/lessons/12951
JadenCase 문자열 만들기
"""
from typing import List
import unittest


def solution(s: str) -> str:
    result: List[str] = list(s.lower())
    if result[0].isalpha():
        result[0] = result[0].upper()
    for i in range(1, len(result)):
        if result[i - 1].isspace() and result[i].isalpha():
            result[i] = result[i].upper()
    return ''.join(result)


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(s="3people unFollowed me"),
                         "3people Unfollowed Me")
        self.assertEqual(solution(s="for the last week"), "For The Last Week")


if __name__ == "__main__":
    unittest.main()
