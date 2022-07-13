"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        add = 0

        while l1 or l2 or add:
            num1 = l1.val if (l1 and l1.next) else 0
            num2 = l2.val if (l2 and l2.next) else 0
            add, mod = divmod(num1 + num2 + add, 10)
            tail.next = ListNode(mod)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


l1 = [2, 4, 3, 1]
l2 = [5, 6, 4]

l1 = ListNode(2)

assert Solution().addTwoNumbers(l1, l2) == [7, 0, 8]
