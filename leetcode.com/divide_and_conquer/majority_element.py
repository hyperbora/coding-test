"""
https://leetcode.com/problems/majority-element/
리스트에서 과반수를 차지하는 엘리먼트를 리턴
"""
import collections
from typing import List
import unittest


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        다이나믹 프로그래밍
        """
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num

    def majorityElement_divide_and_conquer(self, nums: List[int]) -> int:
        """
        분할 정복
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement_divide_and_conquer(nums=nums[:half])
        b = self.majorityElement_divide_and_conquer(nums=nums[half:])

        return [b, a][nums.count(a) > half]

    def majorityElement_pythonic(self, nums: List[int]) -> int:
        """
        파이썬다운 방식
        정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트가 나온다.
        """
        return sorted(nums)[len(nums) // 2]


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.majorityElement(nums=[3, 2, 3]), 3)
        self.assertEqual(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]), 2)
        self.assertEqual(
            s.majorityElement_divide_and_conquer(nums=[3, 2, 3]), 3)
        self.assertEqual(s.majorityElement_divide_and_conquer(
            nums=[2, 2, 1, 1, 1, 2, 2]), 2)
        self.assertEqual(s.majorityElement_pythonic(nums=[3, 2, 3]), 3)
        self.assertEqual(s.majorityElement_pythonic(
            nums=[2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
