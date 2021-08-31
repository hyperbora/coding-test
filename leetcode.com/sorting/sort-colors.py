"""
https://leetcode.com/problems/sort-colors/
네덜란드 국기 문제 응용 문제
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""
from typing import List
import unittest


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()

        arr = [2, 0, 2, 1, 1, 0]
        s.sortColors(arr)
        self.assertListEqual(arr, [0, 0, 1, 1, 2, 2])

        arr = [2, 0, 1]
        s.sortColors(arr)
        self.assertListEqual(arr, [0, 1, 2])

        arr = [0]
        s.sortColors(arr)
        self.assertListEqual(arr, [0])

        arr = [1]
        s.sortColors(arr)
        self.assertListEqual(arr, [1])


if __name__ == "__main__":
    unittest.main()
