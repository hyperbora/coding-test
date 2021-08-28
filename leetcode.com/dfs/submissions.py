"""
https://leetcode.com/problems/reconstruct-itinerary/submissions/
"""
import collections
from typing import List
import unittest


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            # 마지막 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘순 결과로
        return route[::-1]

    class TestSolution(unittest.TestCase):
        def test_result(self):
            s = Solution()
            self.assertListEqual(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], [
                                 "SFO", "SJC"], ["LHR", "SFO"]]), ["JFK", "MUC", "LHR", "SFO", "SJC"])
            self.assertListEqual(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], [
                                 "ATL", "JFK"], ["ATL", "SFO"]]), ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])


if __name__ == "__main__":
    unittest.main()
