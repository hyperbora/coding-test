"""
https://leetcode.com/problems/sliding-window-maximum/
배열(nums)에서 k크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서
각각의 슬라이딩 윈도우에서 최대값을 리스트에 담아서 리턴
"""


from typing import List
import unittest
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q: List[int] = []
        result: List[int] = []

        for i, v in enumerate(nums):
            heapq.heappush(q, (-v, i))
            if i < k - 1:
                continue

            while heapq:
                value, index = q[0]
                value *= -1
                if i - k < index <= i:
                    result.append(value)
                    break
                else:
                    heapq.heappop(q)
        return result


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertListEqual(s.maxSlidingWindow(
            nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3), [3, 3, 5, 5, 6, 7])
        self.assertListEqual(s.maxSlidingWindow(nums=[1], k=1), [1])
        self.assertListEqual(s.maxSlidingWindow(nums=[1, -1], k=1), [1, -1])
        self.assertListEqual(s.maxSlidingWindow(nums=[9, 11], k=2), [11])
        self.assertListEqual(s.maxSlidingWindow(nums=[4, -2], k=2), [4])


if __name__ == "__main__":
    unittest.main()
