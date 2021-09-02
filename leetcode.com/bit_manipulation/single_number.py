"""
https://leetcode.com/problems/single-number/submissions/
하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라.
"""
import operator
from functools import reduce
from typing import List
import unittest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR 연산을 했을 때 두 번 등장한 엘리먼트는 0으로 초기화 되고
        한 번만 등장하는 엘리먼트는 그 값을 보존한다.
        즉 배열의 모든 값을 XOR 하면, 단 한 번만 등장하는 엘리먼트만 그 값이 남게 된다.
        """
        return reduce(operator.xor, nums, 0)


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.singleNumber([2, 2, 1]), 1)
        self.assertEqual(s.singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(s.singleNumber([1]), 1)


if __name__ == "__main__":
    unittest.main()
