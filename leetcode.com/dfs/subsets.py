"""
https://leetcode.com/problems/subsets/
모든 부분 집합을 리턴하라.
트리를 구성하고 트리를 DFS하는 문제로 볼 수 있다.
"""
from typing import List
import unittest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매 번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

    class TestSolution(unittest.TestCase):
        def test_result(self):
            s = Solution()
            self.assertListEqual(
                s.subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
            self.assertListEqual(s.subsets([0]), [[], [0]])


if __name__ == "__main__":
    unittest.main()
