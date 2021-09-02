"""
https://leetcode.com/problems/utf-8-validation/
배열이 UTF-8 문자열이 맞는지 검증
- UTF-8 바이트 순서의 이진 포맷
+-----------+----------+----------+----------+----------+
| 바이트 수  | 바이트 1 | 바이트 2  | 바이트 3 | 바이트 4  |
+===========+==========+==========+==========+==========+
| 1         | 0xxxxxxx |          |          |          |
+-----------+----------+----------+----------+----------+
| 2         | 110xxxxx | 10xxxxxx |          |          |
+-----------+----------+----------+----------+----------+
| 3         | 1110xxxx | 10xxxxxx | 10xxxxxx |          |
+-----------+----------+----------+----------+----------+
| 4         | 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |
+-----------+----------+----------+----------+----------+

예를 들어 첫 바이트가 1110으로 시작한다면 3바이트 문자이므로, 첫 바이트를
제외하고 뒤따르는 2바이트는 모두 10으로 시작해야 유효한 UTF-8 문자가 된다.
"""
from typing import List
import unittest


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            """
            size를 파라미터로 받아 해당 사이즈만큼 바이트가 10으로 시작하는지 판별한다.
            첫 바이트 기준 만약 3바이트 문자라면 나머지 바이트가 모두 10으로 시작하는지 판별한다.
            """
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        self.assertTrue(s.validUtf8([197, 130, 1]))
        self.assertFalse(s.validUtf8([235, 140, 4]))


if __name__ == "__main__":
    unittest.main()
