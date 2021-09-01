"""
https://leetcode.com/problems/intersection-of-two-arrays/
두 배열의 교집합
"""
import bisect
from typing import List, Set
import unittest


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return list(sorted(result))

    def intersection_two_pointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return list(sorted(result))


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        self.assertListEqual(s.intersection(nums1=nums1, nums2=nums2), [2])
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        self.assertListEqual(s.intersection_two_pointers(
            nums1=nums1, nums2=nums2), [2])
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        self.assertListEqual(s.intersection(nums1=nums1, nums2=nums2), [4, 9])
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        self.assertListEqual(s.intersection_two_pointers(
            nums1=nums1, nums2=nums2), [4, 9])


if __name__ == "__main__":
    unittest.main()
