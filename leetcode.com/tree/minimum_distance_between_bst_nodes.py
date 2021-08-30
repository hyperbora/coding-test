"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
bst에서 두 노드 간 값의 차이가 가장 작은 노드 계산
"""
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)
        return self.result

    # 반복 구조로 중위 순회, 스택 사용
    def minDiffInBST_dfs(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result
