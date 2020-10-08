import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rst = 0
        target_set = set()
        for c in s:
            if c in target_set:
                candidate = len(target_set)
                target_set = set([c])
                rst = candidate if candidate > rst else rst
            else:
                target_set.add(c)
        candidate = len(target_set)
        if candidate > 0:
            rst = candidate if candidate > rst else rst
        return rst

class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, s.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, s.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(0, s.lengthOfLongestSubstring(""))
        self.assertEqual(3, s.lengthOfLongestSubstring("dvdf"))

if __name__ == "__main__":
    unittest.main()