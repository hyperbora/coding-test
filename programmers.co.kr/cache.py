import collections
from typing import Deque, List
import unittest


def solution(cacheSize: int, cities: List[str]) -> int:
    elapsed: int = 0
    cache: Deque = collections.deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            elapsed += 1
        else:
            cache.append(c)
            elapsed += 5
    return elapsed


"""
3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25
"""


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(cacheSize=3, cities=[
                         "Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 50)
        self.assertEqual(solution(cacheSize=3, cities=[
                         "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]), 21)
        self.assertEqual(solution(cacheSize=2, cities=[
                         "Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]), 60)
        self.assertEqual(solution(cacheSize=5, cities=[
                         "Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]),	52)
        self.assertEqual(solution(cacheSize=2, cities=[
                         "Jeju", "Pangyo", "NewYork", "newyork"]), 16)
        self.assertEqual(solution(cacheSize=0, cities=[
                         "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 25)


if __name__ == "__main__":
    unittest.main()
