"""
https://leetcode.com/problems/minimum-height-trees/
"""
import collections
from typing import List
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertListEqual(s.findMinHeightTrees(
            n=4, edges=[[1, 0], [1, 2], [1, 3]]), [1])
        self.assertListEqual(s.findMinHeightTrees(
            n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]), [3, 4])
        self.assertListEqual(s.findMinHeightTrees(n=1, edges=[]), [0])
        self.assertListEqual(s.findMinHeightTrees(n=2, edges=[[0, 1]]), [0, 1])


if __name__ == "__main__":
    unittest.main()
