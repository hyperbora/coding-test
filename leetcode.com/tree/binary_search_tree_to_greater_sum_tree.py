"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
이진 탐색 트리에서 각 노드를 현재값보다 큰 값을 가진 모든 노드의 합으로 만들기
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        중위 순회를 하면서 현재 노드의 값을 자신을 포함한 지금까지의 누적된 합과 합친다.
        """
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
