import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rst = 0
        i = 0
        length = len(s)
        while i + rst < length and i < length:
            j = i + rst + 1
            if j <= length:
                if len(s[i:j]) == len(set(s[i:j])):
                    rst += 1
                else:
                    i += 1
            else:
                i += 1
        return rst


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
