"""
https://leetcode.com/problems/maximum-subarray/
합이 최대가 되는 연속 서브 배열의 합을 찾아서 리턴
"""

from typing import List
import unittest
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        앞에서부터 계속 값을 계산하면서 누적 합을 계산한다.
        0이하가 되면 버린다. 0 이하인 값은 굳이 서브 배열에 포함할 이유가 없기 때문이다.
        최종적으로 해당 리스트에서 최대값을 추출하면 정답
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

    def maxSubArray_kadane_algorithm(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.maxSubArray(
            nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(s.maxSubArray(nums=[1]), 1)
        self.assertEqual(s.maxSubArray(nums=[5, 4, -1, 7, 8]), 23)
        self.assertEqual(s.maxSubArray_kadane_algorithm(
            nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(s.maxSubArray_kadane_algorithm(nums=[1]), 1)
        self.assertEqual(s.maxSubArray_kadane_algorithm(
            nums=[5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    unittest.main()
