"""
https://leetcode.com/problems/invert-binary-tree/
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

    def invertTree_bfs(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    def invertTree_dfs(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root
