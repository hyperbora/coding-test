"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 start 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, s.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, s.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(0, s.lengthOfLongestSubstring(""))
        self.assertEqual(1, s.lengthOfLongestSubstring("a"))
        self.assertEqual(3, s.lengthOfLongestSubstring("dvdf"))
        self.assertEqual(5, s.lengthOfLongestSubstring("anviaj"))


if __name__ == "__main__":
    unittest.main()
