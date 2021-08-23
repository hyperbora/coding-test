"""
https://leetcode.com/problems/reverse-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # def reverse(node: ListNode, prev: ListNode = None) -> ListNode:
        #     if not node:
        #         return prev
        #     nxt, node.next = node.next, prev
        #     return reverse(nxt, node)
        # return reverse(head)
        node, prev = head, None
        while node:
            nxt, node.next = node.next, prev
            prev, node = node, nxt
        return prev
