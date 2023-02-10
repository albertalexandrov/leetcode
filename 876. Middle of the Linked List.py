"""
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution1:
    """Мое решение

    Time: O(n)
    Space: O(n)

    """
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pos = {0: head}
        i = 1

        while head.next:
            head = head.next
            pos[i] = head
            i += 1

        max_pos = max(pos.keys())
        mid = int(max_pos / 2) + int(max_pos % 2 > 0)

        return pos[mid]


class Solution2:
    """Подсмотренное решение

    Time: O(n)
    Space: O(1)

    https://leetcode.com/problems/middle-of-the-linked-list/solutions/1651600/python-java-c-simple-solution-one-pass-beginner-friendly-detailed-explanation/?envType=study-plan&id=level-1&page=2

    """
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while head and head.next:
            slow = slow.next
            fast = fast.next.next

        return slow
