import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = [char.lower()
                    for char in s if char.isalnum()]
        half = len(new_list) // 2
        length = len(new_list)
        i = 0
        while i < half:
            if new_list[i] != new_list[-i - 1]:
                return False
            i += 1
        return True


class TestSolution(unittest.TestCase):
    def test_result(self):
        sol = Solution()
        self.assertEqual(True, sol.isPalindrome(
            "A man, a plan, a canal: Panama"))
        self.assertEqual(False, sol.isPalindrome("race a car"))
        self.assertEqual(True, sol.isPalindrome("a"))
        self.assertEqual(False, sol.isPalindrome("ab"))
        self.assertEqual(False, sol.isPalindrome("0P"))


if __name__ == "__main__":
    unittest.main()
