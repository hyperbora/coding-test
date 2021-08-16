import unittest


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rst_node = ListNode()
        head1 = l1
        head2 = l2
        rst_head = None
        div = 0
        while head1 and head2:
            temp_sum = head1.val + head2.val + div
            div = temp_sum // 10
            val = temp_sum % 10

            if rst_head:
                next_node = ListNode(val=val)
                rst_head.next = next_node
                rst_head = rst_head.next
            else:
                rst_node.val = val
                rst_head = rst_node
            head1 = head1.next
            head2 = head2.next

        remain = head1 if head1 is not None else head2
        while remain:
            temp_sum = remain.val + div
            div = temp_sum // 10
            val = temp_sum % 10

            next_node = ListNode(val=val)
            rst_head.next = next_node
            rst_head = rst_head.next
            remain = remain.next
        if div != 0:
            next_node = ListNode(val=div)
            rst_head.next = next_node
            rst_head = rst_head.next
        return rst_node


def get_node_from_list(lst):
    output = None
    head = None
    for val in lst:
        node = ListNode(val=val)
        if head:
            head.next = node
            head = node
        else:
            output = node
            head = output
    return output


def get_list_from_node(node):
    lst = []
    head = node
    while head:
        lst.append(head.val)
        head = head.next
    return lst


def print_node(node):
    head = node
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


class TestSolution(unittest.TestCase):
    def test_result(self):
        s = Solution()
        lst1 = get_node_from_list([2, 4, 3])
        lst2 = get_node_from_list([5, 6, 4])
        rst = get_list_from_node(s.addTwoNumbers(lst1, lst2))
        self.assertEqual([7, 0, 8], rst)
        lst1 = get_node_from_list([0])
        lst2 = get_node_from_list([0])
        rst = get_list_from_node(s.addTwoNumbers(lst1, lst2))
        self.assertEqual([0], rst)
        lst1 = get_node_from_list([9, 9, 9, 9, 9, 9, 9])
        lst2 = get_node_from_list([9, 9, 9, 9])
        rst = get_list_from_node(s.addTwoNumbers(lst1, lst2))
        self.assertEqual([8, 9, 9, 9, 0, 0, 0, 1], rst)


if __name__ == "__main__":
    unittest.main()
