"""
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
"""


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_tree(root):
    arr = []
    stack = []
    head = root
    while True:
        if head:
            stack.append(head)
            head = head.left
        elif stack:
            head = stack.pop()
            arr.append(head.data)
            head = head.right
        else:
            break
    return arr


def checkBST(root):
    arr = inorder_tree(root)
    if len(arr) != len(set(arr)):
        return False
    return arr == sorted(arr)
