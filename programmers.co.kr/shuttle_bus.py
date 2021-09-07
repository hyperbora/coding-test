"""
https://programmers.co.kr/learn/courses/30/lessons/17678
[1차] 셔틀버스
"""
from typing import List
import unittest
from collections import deque


def solution(n: int, t: int, m: int, timetable: List[str]) -> str:
    # 입력값 분 단위 전처리
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()
    queue = deque(timetable)

    current = 540
    for _ in range(n):
        for _ in range(m):
            if queue and queue[0] <= current:
                # 대기가 있는 경우 1분 전 도착
                candidate = queue.popleft() - 1
            else:
                # 대기가 없는 경우 정시 도착
                candidate = current

        current += t
    # 시, 분으로 다시 변경
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ":" + str(m).zfill(2)


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(n=1, t=1, m=5, timetable=[
                         "08:00", "08:01", "08:02", "08:03"]), "09:00")
        self.assertEqual(solution(n=2, t=10, m=2, timetable=[
                         "09:10", "09:09", "08:00"]), "09:09")
        self.assertEqual(solution(n=2, t=1, m=2, timetable=[
                         "09:00", "09:00", "09:00", "09:00"]), "08:59")
        self.assertEqual(solution(n=1, t=1, m=5, timetable=[
                         "00:01", "00:01", "00:01", "00:01", "00:01"]), "00:00")
        self.assertEqual(solution(n=1, t=1, m=1, timetable=["23:59"]), "09:00")
        self.assertEqual(solution(n=10, t=60, m=45, timetable=["23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                                                               "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]), "18:00")


if __name__ == "__main__":
    unittest.main()
