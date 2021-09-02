"""
https://leetcode.com/problems/
두 정수를 입력받아 몇 비트가 다른지 계산
"""
import unittest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.hammingDistance(1, 4), 2)
        self.assertEqual(s.hammingDistance(3, 1), 1)


if __name__ == "__main__":
    unittest.main()
