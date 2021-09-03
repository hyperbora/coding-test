"""
https://leetcode.com/problems/house-robber/
훔칠 수 있는 가장 큰 금액을 출력
단, 현재 집에 있는 돈을 춤치면 바로 옆집은 훔칠 수 없다.
"""

import collections
from typing import List
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1]


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.rob(nums=[1, 2, 3, 1]), 4)
        self.assertEqual(s.rob(nums=[2, 7, 9, 3, 1]), 12)


if __name__ == "__main__":
    unittest.main()
