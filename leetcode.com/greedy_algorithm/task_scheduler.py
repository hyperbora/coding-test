"""
https://leetcode.com/problems/task-scheduler/
"""
import collections
from typing import List
import unittest


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                # trick
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.leastInterval(
            tasks=["A", "A", "A", "B", "B", "B"], n=2), 8)
        self.assertEqual(s.leastInterval(
            tasks=["A", "A", "A", "B", "B", "B"], n=0), 6)
        self.assertEqual(s.leastInterval(
            tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2), 16)


if __name__ == "__main__":
    unittest.main()
