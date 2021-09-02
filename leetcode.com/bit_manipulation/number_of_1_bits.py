"""
https://leetcode.com/problems/number-of-1-bits/
"""
import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        1을 뺀 값과 AND 연산을 할 때마다 비트가 1씩 빠지게 된다.
        0이 될 때 까지 이 작업을 반복하면 전체 비트에서 1의 개수가 몇 개인지 알 수 있다.
        """
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1
        return count


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.hammingWeight(
            int('00000000000000000000000000001011', 2)), 3)
        self.assertEqual(s.hammingWeight(
            int('00000000000000000000000010000000', 2)), 1)


if __name__ == "__main__":
    unittest.main()
