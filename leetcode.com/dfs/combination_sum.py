"""
https://leetcode.com/problems/combination-sum/
"""
from typing import List
import unittest


class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertListEqual(s.combinationSum(
            [2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertListEqual(s.combinationSum([2, 3, 5], 8), [
            [2, 2, 2, 2], [2, 3, 3], [3, 5]])
        self.assertListEqual(s.combinationSum([2], 1), [])
        self.assertListEqual(s.combinationSum([1], 1), [[1]])
        self.assertListEqual(s.combinationSum([1], 2), [[1, 1]])


if __name__ == "__main__":
    unittest.main()
