"""
https://leetcode.com/problems/diameter-of-binary-tree/
이진 트리에서 두 노드 간 가장 긴 경로 찾기
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽 각각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값 : 리프 노드에서 현재 노드까지의 거리
            return max(left, right) + 1

        dfs(root)
        return self.longest
