"""
https://leetcode.com/problems/range-sum-of-bst/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)

    def rangeSumBST_dfs(self, root: TreeNode, low: int, high: int) -> int:
        stack, total = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    total += node.val
        return total

    def rangeSumBST_bfs(self, root: TreeNode, low: int, high: int) -> int:
        stack, total = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    total += node.val
        return total
