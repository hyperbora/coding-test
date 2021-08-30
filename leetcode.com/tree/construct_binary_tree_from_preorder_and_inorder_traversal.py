"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
전위, 중위 순위 결과를 입력값으로 받아 이진 트리로 만들기
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node
