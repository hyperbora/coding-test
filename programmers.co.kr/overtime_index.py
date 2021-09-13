"""
https://programmers.co.kr/learn/courses/30/lessons/12927/
야근 지수
"""
from typing import List
import heapq
import unittest


def solution(n: int, works: List[int]) -> int:
    if sum(works) <= n:
        return 0
    lst = []
    for work in works:
        heapq.heappush(lst, -work)
    while n > 0:
        work = -heapq.heappop(lst)
        heapq.heappush(lst, (work - 1) * -1)
        n -= 1
    return sum([work ** 2 for work in lst])


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(n=4, works=[4, 3, 3]), 12)
        self.assertEqual(solution(n=1, works=[2, 1, 2]), 6)
        self.assertEqual(solution(n=3, works=[1, 1]), 0)


if __name__ == "__main__":
    unittest.main()
