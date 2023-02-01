"""
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list
that has Node.val == val, and return the new head.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """

    Time: O(n)
    Space: O(1)

    Первый элемент поначалу не трогаем, так как он может быть равен val и это может
    создать сложности, которые отразится на сложности кода

    """
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return head

        tail = head

        while tail.next:
            current = tail.next

            if current.val == val:
                tail.next = current.next
            else:
                tail = current

        return head.next if head.val == val else head
