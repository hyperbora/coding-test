"""
https://leetcode.com/problems/longest-repeating-character-replacement/
대문자 문자열 s에서 k번만큼의 변경으로 만들 수 있는,
연속으로 반복된 문자열의 가장 긴 길이를 출력
"""
import unittest
import collections
from typing import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left: int = 0
        right: int = 0
        counts: Counter = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탬색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.characterReplacement(s="ABAB", k=2), 4)
        self.assertEqual(s.characterReplacement(s="AABABBA", k=1), 4)


if __name__ == "__main__":
    unittest.main()
