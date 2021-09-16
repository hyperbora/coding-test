"""
https://programmers.co.kr/learn/courses/30/lessons/42892
길 찾기 게임
"""
from typing import List, Tuple
import sys
import unittest

sys.setrecursionlimit(10 ** 6)


class Node():
    def __init__(self, x: int, y: int, index: int):
        self.left = None
        self.right = None
        self.x = x
        self.y = y
        self.index = index

    def __str__(self) -> str:
        return f'left={self.left}, right={self.right}, x={self.x}, y={self.y}, index={self.index}'


def preorder(root: Node) -> List[int]:
    arr: List[int] = []

    def _pre(node: Node):
        arr.append(node.index)
        if node.left:
            _pre(node.left)
        if node.right:
            _pre(node.right)
    _pre(root)
    return arr


def postorder(root) -> List[int]:
    arr: List[int] = []

    def _post(node: Node):
        if node.left:
            _post(node.left)
        if node.right:
            _post(node.right)
        arr.append(node.index)
    _post(root)
    return arr


def solution(nodeinfo: List[List[int]]) -> List[List[int]]:
    new_nodeinfo: List[Tuple[int]] = []
    for i, node in enumerate(nodeinfo, 1):
        new_nodeinfo.append((node + [i]))
    new_nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    root: Node = Node(*new_nodeinfo[0])

    for node in new_nodeinfo:
        x: int = node[0]
        cur: Node = root
        while True:
            if x < cur.x:
                if cur.left:
                    cur = cur.left
                    continue
                else:
                    cur.left = Node(*node)
                    break
            if x > cur.x:
                if cur.right:
                    cur = cur.right
                    continue
                else:
                    cur.right = Node(*node)
                    break
            break

    return [preorder(root), postorder(root)]


class TestSolution(unittest.TestCase):
    def test_result(self):
        self.assertListEqual(solution(nodeinfo=[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [
                             8, 6], [7, 2], [2, 2]]), [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]])


if __name__ == "__main__":
    unittest.main()
