"""
https://leetcode.com/problems/climbing-stairs/
n계단을 오르는 방법찾기
"""
import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.climbStairs(3), 3)


if __name__ == "__main__":
    unittest.main()
