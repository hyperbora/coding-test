"""
https://programmers.co.kr/learn/courses/30/lessons/64064/
불량 사용자
"""

from typing import List, Set, Tuple
import unittest
from itertools import permutations


def check(users: Tuple[str], banned_id: List[str]) -> bool:
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for u, b in zip(users[i], banned_id[i]):
            if b != "*" and b != u:
                return False
    return True


def solution(user_id: List[str], banned_id: List[str]) -> int:
    user_permutation: List[Tuple] = list(permutations(user_id, len(banned_id)))
    banned_set: Set[Tuple] = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            s: Set[str] = set(users)
            if s not in banned_set:
                banned_set.append(s)

    return len(banned_set)


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(user_id=[
                         "frodo", "fradi", "crodo", "abc123", "frodoc"], banned_id=["fr*d*", "abc1**"]), 2)
        self.assertEqual(solution(user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"], banned_id=[
                         "*rodo", "*rodo", "******"]), 2)
        self.assertEqual(solution(user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"], banned_id=[
                         "fr*d*", "*rodo", "******", "******"]), 3)


if __name__ == "__main__":
    unittest.main()
