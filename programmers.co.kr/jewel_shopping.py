"""
https://programmers.co.kr/learn/courses/30/lessons/67258
[카카오 인턴] 보석 쇼핑
"""
from typing import DefaultDict, List
from collections import defaultdict
import unittest


def solution(gems: List[int]) -> List[int]:
    kind: int = len(set(gems))
    length: int = len(gems)
    answer: List[int] = []

    start: int = 0
    end: int = 0
    d: DefaultDict = defaultdict(int)
    _min = float('inf')
    while end < length:
        d[gems[end]] += 1
        end += 1

        if len(d) == kind:
            while start < end:
                if d[gems[start]] > 1:
                    d[gems[start]] -= 1
                    start += 1
                elif _min > end - start:
                    _min = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break
    return answer


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(
            gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]), [3, 7])
        self.assertListEqual(
            solution(gems=["AA", "AB", "AC", "AA", "AC"]), [1, 3])
        self.assertListEqual(solution(gems=["XYZ", "XYZ", "XYZ"]), [1, 1])
        self.assertListEqual(
            solution(gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]), [1, 5])


if __name__ == "__main__":
    unittest.main()
