import unittest


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


class TestSolution(unittest.TestCase):
    def test_result(self):
        sol = Solution()
        strs = ["h", "e", "l", "l", "o"]
        sol.reverseString(strs)
        self.assertEqual(["o", "l", "l", "e", "h"], strs)
        strs = ["H", "a", "n", "n", "a", "h"]
        sol.reverseString(strs)
        self.assertEqual(["h", "a", "n", "n", "a", "H"],
                         strs)


if __name__ == "__main__":
    unittest.main()
