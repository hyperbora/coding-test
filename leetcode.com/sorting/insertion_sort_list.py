"""
https://leetcode.com/problems/
연결리스트를 insertion sort로 정렬하라.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        cur : 정렬이 끝난 리스트
        head : 정렬을 해야하는 리스트
        """
        # 초기값 변경
        cur = parent = ListNode(0)
        while head:
            # 값을 비교하면서 cur 리스트에 들어갈 위치를 찾는다.
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        return parent.next
