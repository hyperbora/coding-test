"""
https://programmers.co.kr/learn/courses/30/lessons/17683
[3차] 방금그곡
"""
from collections import deque
from typing import List, Tuple
import unittest


def new_melody(melody: str) -> List[str]:
    q = deque(melody)
    result = []
    while q:
        item: str = q.popleft()
        if q and q[0] == "#":
            item += q.popleft()
        result.append(item)
    return result


def solution(m, musicinfos):
    music_list: List[Tuple] = []
    for i, musicinfo in enumerate(musicinfos):
        start_time, end_time, title, melody = musicinfo.split(",")
        duration: int = int(end_time[:2]) * 60 + int(end_time[3:]) - \
            int(start_time[:2]) * 60 - int(start_time[3:])
        music_list.append(
            (title, new_melody(melody=melody), duration, i))
    music_list.sort(key=lambda x: (-x[2], x[3]))
    query_melody = new_melody(m)
    for title, melody, duration, _ in music_list:
        left = right = 0

        found: int = -1
        while True:
            try:
                found = melody.index(query_melody[0], found + 1)
            except ValueError:
                break
            else:
                left = 0
                right = found
                right_count = found + 1
                while right_count <= duration and left < len(query_melody):
                    if query_melody[left] == melody[right]:
                        left += 1
                        right = (right + 1) % len(melody)
                        right_count += 1
                    else:
                        break
                else:
                    if left == len(query_melody):
                        return title

    return "(None)"


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(m="ABCDEFG", musicinfos=[
                         "12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]), "HELLO")
        self.assertEqual(solution(m="CC#BCC#BCC#BCC#B", musicinfos=[
                         "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]), "FOO")
        self.assertEqual(solution(m="ABC", musicinfos=[
                         "12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]), "WORLD")


if __name__ == "__main__":
    unittest.main()
