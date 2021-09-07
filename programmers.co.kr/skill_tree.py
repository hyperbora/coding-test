"""
https://programmers.co.kr/learn/courses/30/lessons/49993
스킬트리
"""
from typing import List
import re
import unittest


def solution(skill: str, skill_trees: List[str]) -> int:
    def is_valid(tree: str) -> int:
        sqeeze = re.sub(f'[^{skill}]', '', tree)
        if sqeeze:
            if sqeeze in skill and skill.index(sqeeze) == 0:
                return 1
        else:
            return 1
        return 0
    return sum(is_valid(skill_tree) for skill_tree in skill_trees)


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(skill="CBD", skill_trees=[
                         "BACDE", "CBADF", "AECB", "BDA"]), 2)


if __name__ == "__main__":
    unittest.main()
