"""
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List
import unittest


class Solution:
    """
    리스트에서 가장 높은 막대를 찾는다. 막대는 높고 낮음에 무관하게
    전체 부피에 영향을 주지 않으며 왼쪽, 오른쪽을 가르는 장벽 역할을 한다.
    """

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(
                height[right], right_max)

            # 최대 높이의 막대까지 각각 좌우 기둥 최대 높이 left_max, right_max가
            # 현재 높이와의 차이만큼 물 높이 volume을 더해 간다.
            # 적어도 낮은 쪽은 그만큼 항상 채워질 것이기 때문에, 좌우 어느 쪽이든 낮은 쪽은 높은 쪽을 향해서
            # 포인터가 가운데로 이동한다.
            # 오른쪽이 크면 left += 1로 왼쪽이 이동, 반대면 right -= 1로 오른쪽이 이동한다.
            # 결국 최대 높이 지점까지 좌우 포인터가 서로 만나게 된다.
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(9, s.trap([4, 2, 0, 3, 2, 5]))


if __name__ == "__main__":
    unittest.main()
