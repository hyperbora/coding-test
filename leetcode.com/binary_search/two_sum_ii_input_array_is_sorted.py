"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List
import bisect
import unittest


class Solution:
    def twoSum_two_pointers(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return [k + 1, i + 1]


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertListEqual(s.twoSum_two_pointers(numbers, target), [1, 2])
        self.assertListEqual(s.twoSum(numbers, target), [1, 2])
        numbers = [2, 3, 4]
        target = 6
        self.assertListEqual(s.twoSum_two_pointers(numbers, target), [1, 3])
        self.assertListEqual(s.twoSum(numbers, target), [1, 3])
        numbers = [-1, 0]
        target = -1
        self.assertListEqual(s.twoSum_two_pointers(numbers, target), [1, 2])
        self.assertListEqual(s.twoSum(numbers, target), [1, 2])


if __name__ == "__main__":
    unittest.main()
