"""
https://programmers.co.kr/learn/courses/30/lessons/68936
쿼드압축 후 개수 세기
"""
from typing import List
import unittest


def is_valid(arr: List[int], row: int, col: int, size: int) -> bool:
    if size == 1:
        return True
    target = arr[row][col]
    for i in range(row, row + size):
        for j in range(col, col + size):
            if target != arr[i][j]:
                return False
    return True


def solution(arr):
    # [0의 개수, 1의 개수]
    answer = [0, 0]

    def calc(row: int, col: int, size: int):
        if is_valid(arr=arr, row=row, col=col, size=size):
            if arr[row][col] == 0:
                answer[0] += 1
            else:
                answer[1] += 1
        else:
            new_size = size // 2
            calc(row=row, col=col, size=new_size)
            calc(row=row, col=col + new_size, size=new_size)
            calc(row=row + new_size, col=col, size=new_size)
            calc(row=row + new_size, col=col + new_size, size=new_size)
    calc(row=0, col=0, size=len(arr))

    return answer


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(
            solution(arr=[
                [1, 1, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1]
            ]), [4, 9])
        self.assertListEqual(
            solution(arr=[
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]
            ]), [10, 15])


if __name__ == "__main__":
    unittest.main()
