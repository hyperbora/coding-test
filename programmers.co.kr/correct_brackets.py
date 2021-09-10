"""
https://programmers.co.kr/learn/courses/30/lessons/12909
올바른 괄호
"""
import unittest


def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return False if stack else True


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertTrue(solution(s="()()"))
        self.assertTrue(solution(s="(())()"))
        self.assertFalse(solution(s=")()("))
        self.assertFalse(solution(s="(()("))


if __name__ == "__main__":
    unittest.main()
