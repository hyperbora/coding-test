"""
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    def swap_pairs_using_iteration(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록
            prev.next = b

            # 다음 번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next

    def swap_pairs_using_recursive(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swap_pairs_using_recursive(p.next)
            p.next = head
            return p
        return head
