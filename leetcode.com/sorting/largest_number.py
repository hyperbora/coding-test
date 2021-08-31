"""
https://leetcode.com/problems/largest-number/
리스트를 조합해서 만들 수 있는 가장 큰 수를 리턴
"""


from typing import List
import unittest


class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.largestNumber([10, 2]), '210')
        self.assertEqual(s.largestNumber([3, 30, 34, 5, 9]), '9534330')
        self.assertEqual(s.largestNumber([1]), '1')
        self.assertEqual(s.largestNumber([10]), '10')


if __name__ == "__main__":
    unittest.main()
