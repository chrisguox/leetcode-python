# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_node = ListNode(0)
        _list_node = list_node
        carry = 0

        while l1 or l2:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            value_sum = l1_value + l2_value + carry

            if value_sum >= 10:
                list_node_value, carry = value_sum - 10, 1
            else:
                list_node_value, carry = value_sum, 0

            _list_node.next = ListNode(list_node_value)
            _list_node = _list_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            _list_node.next = ListNode(1)

        return list_node.next
