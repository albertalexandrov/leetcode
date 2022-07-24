"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        При попытке решить задачу совершил одну ошибку: пытался всю логику уложить в цикле while,
        что значительно усложняло алгоритм.
        """

        # головная нода смерженного связного списка
        merged = ListNode()

        # хвост смерженного связного списка для присоединения каждой последующей ноды
        # на каждой итерации меняется на отсортированную ноду
        tail = merged

        # не обязательно итерироваться по каждому элементу каждого связного списка
        # достатчтоно проитерировать до того момента, пока в одном из списков не закончатся элементы
        # затем просто привяжем оставшийся список к tail
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return merged.next
