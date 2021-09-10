"""
https://programmers.co.kr/learn/courses/30/lessons/17686
[3차] 파일명 정렬
"""
import re
from typing import List
import unittest


def solution(files) -> List[str]:
    answer: List[str] = []
    for i, file in enumerate(files):
        r = re.search('(^[a-zA-z\- ]+)([0-9]{1,5}).*', file)
        head: str = r.group(1).lower()
        number: int = int(r.group(2))
        answer.append((head, number, i, file))
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return [item[3] for item in answer]


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(files=["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]), [
                             "img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
        self.assertListEqual(solution(files=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]), [
                             "A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])


if __name__ == "__main__":
    unittest.main()
