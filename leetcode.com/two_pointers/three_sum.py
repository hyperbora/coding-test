"""
https://leetcode.com/problems/3sum/
"""
from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복은 넘어간다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 투 포인터가 간격을 좁혀나가며 합을 계산한다.
            # 합이 0이면 결과에 추가한다. left, right가 동일한 값이 있을 수 있으므로 스킵 처리한다.
            # 마지막으로 left를 한 칸 우측으로, right를 한 칸 왼쪽으로 이동하고 다음으로 넘어간다.
            # sum == 0 인 상황이므로 어느 한쪽만 이동하는 경우는 어차피 답이 아니다.
            # 나머지 정답을 찾으려면 left, right 둘 다 움직여야 한다.
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertListEqual([[-1, -1, 2], [-1, 0, 1]],
                             s.threeSum([-1, 0, 1, 2, -1, -4]))
        self.assertListEqual([], s.threeSum([]))
        self.assertListEqual([], s.threeSum([0]))


if __name__ == "__main__":
    unittest.main()
