"""
https://leetcode.com/problems/two-sum/
"""
from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual([0, 1], sorted(
            s.twoSum(nums=[2, 7, 11, 15], target=9)))
        self.assertEqual([1, 2], sorted(s.twoSum(nums=[3, 2, 4], target=6)))
        self.assertEqual([0, 1], sorted(s.twoSum(nums=[3, 3], target=6)))


if __name__ == "__main__":
    unittest.main()
