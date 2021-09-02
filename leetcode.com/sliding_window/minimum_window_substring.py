"""
https://leetcode.com/problems/minimum-window-substring/
"""

import collections
import unittest
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        need : 필요한 문자 각각의 개수
        missing : 필요한 문자의 전체 개수
        left : 슬라이딩 윈도우의 왼쪽 index
        right : 슬라이딩 윈도우의 오른쪽 index
        start : 정답 왼쪽 index
        end : 정답 오른쪽 index
        """
        need: Counter = collections.Counter(t)
        missing: int = len(t)
        left: int = 0
        start: int = 0
        end: int = 0

        # 오른쪽 포인터 이동
        # enumerate(s, 1)은 1부터 인덱스가 시작한다는 뜻
        for right, char in enumerate(s, 1):
            """
            오른쪽 포인터(right) 값을 계속 늘려 나간다.
            슬라이딩 윈도우의 크기가 점점 더 커지는 형태가 된다.
            먄약 현재 문자가 필요한 문자 need[char]에 포함되어 있다면 
            필요한 문자의 전체 개수 missing을 1 감소하고,
            해당 문자의 필요한 개수 need[char]도 1 감소한다.
            """
            missing -= need[char] > 0
            need[char] -= 1

            """
            필요 문자가 0이면 왼쪽 포인터 이동 판단
            왼쪽 포인터가 불필요한 문자를 가리키고 있다면 분명 음수일 것이고,
            0을 가리키는 위치까지 왼쪽 포인터를 이동한다.
            다시 슬라이딩 윈도우의 크기가 점점 더 줄어드는 형태가 된다.

            missing이 0이 될 때까지의 오른쪽 포인터와 need[s[left]]가 0이 될 때까지의
            왼쪽 포인터를 정답으로 정한다.
            더 작은 값을 찾을 때까지 유지하다가 가장 작은 값인 경우,
            정답으로 슬라이싱 결과를 리턴한다.
            """
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(s.minWindow(s="ADOBECODEBANC", t="ABC"), "BANC")
        self.assertEqual(s.minWindow(s="a", t="a"), "a")
        self.assertEqual(s.minWindow(s="a", t="aa"), "")


if __name__ == "__main__":
    unittest.main()
